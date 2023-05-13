#!/usr/bin/env python3.7

# Import the boto3 module for AWS SDK
import boto3

# Define the instance IDs to stop
instance_ids="i-0913248b9e3a8bd9c", "i-0e5feb6be4091e73c", "i-0fb1307c89d9bcb1f"

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Stop the instances with the specified instance IDs
response = ec2.stop_instances(
    InstanceIds=instance_ids
)

# Print a message indicating the instances have been stopped
print("The Development instances have been stopped.")