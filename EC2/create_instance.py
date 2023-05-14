import boto3

ami_id = "ami-0a1181c12e57257d1"
key_pair_name = "Key from boto3"
security_group_id = "sg-03115c14a5fb462e3"

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id
    ]

)

print(response)