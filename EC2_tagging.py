import json
import boto3

ec2 = boto3.client('ec2')



def lambda_handler(event, context):
    print(event)

    user = event['detail']['userIdentity']['principalId']
    instanceID =  event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    ec2.create_tags(
        Resources=[
            instanceID,
        ],
        Tags = [
            {
                'Key': 'Owner',
                'Value': user
            },
        ]
    )
    return
