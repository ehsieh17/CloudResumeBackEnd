import json
import boto3

def lambda_handler(event, context):
    
    # connect to dynamodb resource
    client = boto3.resource('dynamodb')
    
    # create a dynamodb cliente to the visitor_count table
    table = client.Table('visitor_count')
    
    # increment visitor_count attribute for index.html key
    response = table.update_item(
        Key={
            'path': 'index.html'
        },
        AttributeUpdates={
            'visitor_count': {
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    
    # get visitor_count from visitor_count table for index.html
    response = table.get_item(
        Key={
            'path': 'index.html'
        }
    )
    visitor_count = response['Item']['visitor_count']
    
    # return visitor_count to user
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
