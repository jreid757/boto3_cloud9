import boto3

vpc_id = "vpc-054b04c5841fbfa29"

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId='vpc-054b04c5841fbfa29')

print(routeTable["RouteTable"]["RouteTableId"])