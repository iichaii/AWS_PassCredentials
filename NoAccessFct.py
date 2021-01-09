import json
import boto3

def lambda_handler(event, context):
    #1 Read the input parameters
    ACCESS_KEY = event['ACCESS_KEY']
    SECRET_KEY    = event['SECRET_KEY']
    SESSION_TOKEN   = event['SESSION_TOKEN']

    #3 Implement Business Logic
    s3=boto3.client('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,aws_session_token=SESSION_TOKEN)
    #s3=boto3.client('s3')
    bucket = 'testsecurityrdp'
    key = 'doc.json'
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())
    customers = jsonObject['customers']

    for record in customers:
        name = record['name'],
        age = record['age'],
        city = record['city']
    return {
        'name' :   name,
        'age'   :   age,
        'city'        :   city
    }


