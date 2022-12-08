from slack.web.client import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
import pandas as pd
from pprint import pprint
client = WebClient(token='xoxb-4018866528417-4492610035728-dSzFi8qruR69qxogFb3ZST0T')

import os
from slack_sdk import WebClient

client = WebClient(token="xoxb-4018866528417-4492610035728-dSzFi8qruR69qxogFb3ZST0T")
response = client.users_list(channel="beta")
user_ids = response["members"]
for i in user_ids:
    if i['deleted']==False:
        pass
    else:
        print(i["name"])
