from slack.web.client import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
def users_of_the_channel():
    slack_client = WebClient(token='xoxb-4018866528417-4492610035728-dSzFi8qruR69qxogFb3ZST0T')
    # global slack_client
    #this is the variable which is initialized with SlackClient(BOT_TOKEN)
    api_call = slack_client.api_call( "users.list",channel="beta") 
    if api_call.get('ok'):
        channels = api_call.get('members')
        for channel in channels:
            print ("this is cool : ", channel['team_id'])
users_of_the_channel()