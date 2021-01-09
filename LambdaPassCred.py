import boto3
import json

def lambda_handler(context, event):
    #assumerole&retrievetemporarycredentials
    sts_connection = boto3.client('sts')
    assume = sts_connection.assume_role(
        RoleArn="arn:aws:iam::153787536644:role/ROLE_B",
        RoleSessionName="cross_acct_lambda"
    )

    ACCESS_KEY = assume['Credentials']['AccessKeyId']
    SECRET_KEY = assume['Credentials']['SecretAccessKey']
    SESSION_TOKEN = assume['Credentials']['SessionToken']

    #passing cred to another lambda
    client = boto3.client('lambda')
    # Define the input parameters that will be passed on to the child function
    inputParams = {
        "ACCESS_KEY"   : ACCESS_KEY,
        "SECRET_KEY"      : SECRET_KEY,
        "SESSION_TOKEN"     : SESSION_TOKEN
    }
    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-1:153787536644:function:childFunction',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )
    responseFromNoAccessFct = json.load(response['Payload'])
    print('\n')
    print(responseFromNoAccessFct)