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
client.chat_postMessage(channel="beta",text="Message")
