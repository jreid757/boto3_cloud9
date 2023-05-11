import boto3

internet_gateway_id = 'igw-07e9a126fed00e478'
vpc_id = 'vpc-054b04c5841fbfa29'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)