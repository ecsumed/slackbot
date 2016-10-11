import local

API_TOKEN = local.SLACK_API_TOKEN

ERRORS_TO = "slackbot_errors"

DEFAULT_REPLY = "You're not making sense, you filthy human"

PLUGINS = [
        'slackbot.plugins',
        'custom_bot',
        ]

