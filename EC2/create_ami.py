import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-09544cc4852e545c4',
    Name='Go To Ami'
)

print(response['ImageId'])