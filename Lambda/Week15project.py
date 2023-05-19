import boto3

# Create an SQS resource object
sqs = boto3.resource('sqs', region_name='us-east-1')

# Specify the queue name
queue_name = 'Wk15Project'

# Create a new queue
queue = sqs.create_queue (QueueName=queue_name)

# Print the URL of the newly created queue
print(queue.url)