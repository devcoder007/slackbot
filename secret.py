

import boto3
from botocore.exceptions import ClientError

def get_secret():

    secret_name = "success_is_sweet_but_its_secret_is_sweat"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session(aws_access_key_id="AKIA5TAQKQF3BRPBAVGE",aws_secret_access_key="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")
      
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    print(secret)
get_secret()