import boto3

internet_gateway_id = "igw-07e9a126fed00e478"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)