from slack.web.client import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
import pandas as pd
client = WebClient(token='xoxb-4018866528417-4492610035728-dSzFi8qruR69qxogFb3ZST0T')
client.chat_postMessage(channel="beta",text="Let's learn about slack api's dummy message")