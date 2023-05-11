import boto3

subnet_id = "subnet-0ac56929842bffcf7"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)