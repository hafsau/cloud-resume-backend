import json
import boto3
from decimal import Decimal


def lambda_handler(event, context):
    # TODO implement
    db = boto3.resource ('dynamodb')
    table = db.Table ('VisitorsCounts')
    dbResponse = table.update_item (
        Key = {'count' : 'numb' },
        UpdateExpression = 'ADD visitor_count :num',
        ExpressionAttributeValues = {':num': Decimal (1)},
        ReturnValues = 'UPDATED_NEW'
        )
        
    response = json.dumps ({'count': int(dbResponse ['Attributes']['visitor_count'])})
    #response = 'Hello World'
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': { 
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET'
        },
        'body': response
    }
