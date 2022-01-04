import os, re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# initialize the Slack app with the provided bot token 
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# listen for the word book in any channel
@app.message(re.compile("(reserve|Reserve|Book|book)"))
def book_conference_room(message):

    # get the channel and thread id of the person who typed the word book
    channel_id = message["channel"]
    thread_id = message["ts"]

    # using the message object get more information about the requestor
    user_info = app.client.users_info(
        user = message["user"]
    )
    requestor_username = user_info["user"]["name"]
    requestor_email_address = user_info["user"]["profile"]["email"]

    # response to the requestor
    chat_response = app.client.chat_postMessage(
        channel=channel_id,
        thread_ts=thread_id,
        text="The conference room is yours! Please check your email for a confirmation."
    )
    chat_response_string = str(chat_response)

    # build out the contents of the email message
    email_message = Mail(
        from_email="nolanprewit1@gmail.com",
        to_emails = [requestor_email_address,"automate.this@bettercloud.com"],
        subject="IT Automation Engineer Exercise - Parker Prewit",
        is_multiple=True,
        html_content = "Slack Username: <br>" + requestor_username + "<br><br> API Payload: <br>" + chat_response_string
    )

    # send an email to the requestor letting them know the room has been booked
    try:
        send_grid = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = send_grid.send(email_message)
        if(response.status_code == 202):
            print("Status Code 202: Email successfully sent...")
    except Exception as e:
        print(e.message)

# start the app with the provided app token
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
