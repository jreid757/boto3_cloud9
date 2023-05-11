import boto3

vpc_id = "vpc-054b04c5841fbfa29"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)