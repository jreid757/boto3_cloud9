import boto3

route_table_id = "rtb-0363c40df2d23e8b2"

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)