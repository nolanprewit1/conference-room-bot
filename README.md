This is a Slack app built with the [Bolt for Python framework][2]. This simulates the utlization of a bot to automate the booking of requested conference room in an easy manner. 

## Running locally

### 1. Setup environment variables

```zsh
# Replace with your signing secret, bot token, and sendgrid api key. NOTE: If you use Mac OS / Linux your commands may differ.
$env:SLACK_BOT_TOKEN=<your-bot-token>
$env:SLACK_APP_TOKEN=<your-signing-secret>
$env:SENDGRID_API_KEY=<sendgrid-api-key>
```

### 2. Setup your local project

```zsh
# Clone this project onto your machine
git clone https://github.com/nolanprewit1/conference-room-bot

# Change into this project
cd conference-room-bot

# Install virtualenv if required
pip install virtualenv

# Setup virtual environment
virtualenv env
\pathto\conference-room-bot\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

### 3. Start app

```zsh
 python .\app.py
```

[1]: https://slack.dev/bolt-python/tutorial/getting-started
[2]: https://slack.dev/bolt-python/
[3]: https://slack.dev/bolt-python/tutorial/getting-started#setting-up-events