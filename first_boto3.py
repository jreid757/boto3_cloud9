import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='jreid-boto3-05072023',
)

print(response)