import boto3

# create an s3 client
s3_client = boto3.client('s3')

# list all buckets
response = s3_client.list_buckets()

# print bucket names
print('existing buckets are:')
for bucket in response['Buckets']:
    print (f'   {bucket["Name"]}')