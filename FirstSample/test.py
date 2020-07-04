import boto3
s3 = boto3.resource('s3')

# Listing all the buckets in the region us-east-1

for bucket in s3.buckets.all():
    print(bucket.name)
