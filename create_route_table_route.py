import boto3

route_table_id = "rtb-0363c40df2d23e8b2"
internet_gateway_id = "igw-07e9a126fed00e478"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)