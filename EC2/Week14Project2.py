#!/usr/bin/env python3.7

# Import the boto3 module for AWS SDK
import boto3

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Retrieve information about EC2 instances
response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Environment', 'Values': ['Dev']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
)

# Initialize an empty list to store instance IDs
instance_ids=[]

# Extract instance IDs from the response
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Stop the instances with the obtained instance IDs
response = ec2.stop_instances(
    InstanceIds=instance_ids
)

# Print a message indicating the development instances have been stopped
print("The Development instances have been stopped.")