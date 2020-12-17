"""
    app_settings.py file contains all the settings and credentials for the app.
"""
import os
import json

# Debug Mode
if 'BotDebug' in os.environ:
    if os.environ['BotDebug'] == 'false':
        debug = False
    else:
        debug = True
else:
    debug = True  # Should be False in Production


# Read from secrets file if in debug mode
if os.path.isfile("secrets.json") and debug:
    with open("secrets.json", 'r') as file:
        secrets = json.loads(file.read())

        for k, v in secrets.items():
            os.environ[k] = v


# MongoDB Credentials
MONGODB_PASSWORD = os.environ['BotMongoPassword']
MONGODB_USERNAME = os.environ['BotMongoUsername']
MONGODB_NAME = os.environ['BotMongoDBName']
MONGODB_HOST = os.environ['BotMongoHost']


# Discord Token
DISCORD_TOKEN = os.environ['DiscordToken']


# Google API Keys
GOOGLE_API_KEY = os.environ['GoogleAPIKey']
GOOGLE_CSE_ID = os.environ['GoogleCSEID']
