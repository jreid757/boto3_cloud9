import boto3

s3 = boto3.client('s3')

with open("test_text.txt", 'rb') as f:
    s3.put_object(Bucket="jreid-boto3-05072023", 
                    Key="folder/foldera/folder1/test_text_string.txt", 
                    Body="Hey this is a string", 
                    ContentType="text/plain")