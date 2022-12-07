from slack_sdk import WebClient
import boto3
import json
from botocore.exceptions import ClientError

secret_name = "slack_bot_token"
region_name = "us-east-1"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
except ClientError as e:
    raise e

# Decrypts secret using the associated KMS key.
secret = get_secret_value_response['SecretString']
TOKEN = json.loads(secret)['Token']
client = WebClient(token=TOKEN)
# client.chat_postMessage(channel="beta",text="Message `inline *code*`")
client.chat_postMessage(channel="beta",blocks=[
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Danny Torrence left the following review for your property:"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room " +
          "237 was far too rowdy, whole place felt stuck in the 1920s."
      },
      "accessory": {
        "type": "image",
        "image_url": "https://images.pexels.com/photos/750319/pexels-photo-750319.jpeg",
        "alt_text": "Haunted hotel image"
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Average Rating*\n1.0"
        }
      ]
    }
  ])
