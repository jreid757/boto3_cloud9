import boto3

ec2 = boto3.client('ec2')

route_table_id = "rtb-0363c40df2d23e8b2"

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)