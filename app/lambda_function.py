import boto3
import json

TABLE_NAME = "basicSongsTable"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        response=table.put_item(Item=event)
        return table.scan()
    except:
        raise