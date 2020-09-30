import os
import io
import boto3
import json
import csv
def lambda_handler(event, context):
    ENDPOINT_NAME = os.environ['envirornment_variable']
    runtime= boto3.client('runtime.sagemaker')
    print(ENDPOINT_NAME)
    print("Received event: " , json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    print("Data:",data)
    payload = data['data']
    print("Payload:",payload)
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)

    if result>0.5:
        return "P"
    else:
        return "N"
