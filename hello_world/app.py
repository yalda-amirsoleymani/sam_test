import os
import boto3


dynamodb = boto3.resource('dynamodb')
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": f"DynamoDB table name is: {table_name}"
    }

