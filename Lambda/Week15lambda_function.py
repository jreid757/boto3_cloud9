import json
import boto3
from datetime import datetime

# Get the current date and time
current_date_time = datetime.now()

# Create an SQS resource object
sqs = boto3.resource('sqs', region_name='us-east-1')

def lambda_handler(event, context):
    
    # Get the queue by name
    queue = sqs.get_queue_by_name(QueueName='Wk15Project')
    
    # Format the current date and time as a string
    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    
    # Create the message to be sent
    message = ("The date and time at the point of this trigger was " + str(date_time) + ".")
    
    # Send the message to the queue
    response = queue.send_message(MessageBody = message)
    
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
