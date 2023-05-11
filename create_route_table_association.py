import boto3

route_table_id = 'rtb-0363c40df2d23e8b2'
subnet_id = 'subnet-0ac56929842bffcf7'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])