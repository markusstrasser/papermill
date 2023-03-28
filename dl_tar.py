import boto3

# Connect to S3
s3 = boto3.resource('s3')

# Get the latest Computer Science TAR file
bucket_name = 'arxiv'
prefix = 'arxiv/pdf'
computer_science_prefix = prefix + '/cs/'
bucket = s3.Bucket(bucket_name)
latest_object = sorted(bucket.objects.filter(Prefix=computer_science_prefix), key=lambda obj: obj.last_modified)[-1]

# Download the TAR file to local disk
latest_object.download_file('latest_cs.tar')

import tarfile

tar_file = tarfile.open('latest_cs.tar')
tar_file.extractall('pdfs')

