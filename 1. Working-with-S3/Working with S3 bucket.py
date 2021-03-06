import boto3
import time
import glob

class s3Api:
    """ Get name of the buckets """
    def listBuckets(self):
        s3 = boto3.client('s3')
        return s3.list_buckets()

    """ Upload a file """
    def fileUpload(self, bucket_name, source_file_name, file_name):
        s3Resource = boto3.resource('s3')
        s3Resource.Object(bucket_name, source_file_name).upload_file(Filename=file_name)
        print('file uploaded')

s3 = s3Api()
for i in glob.glob('tech/*.txt'):
    s3.fileUpload("sample-data-b00845449",i.split('\\')[1], i)
    time.sleep(0.1)
print('Upload Successful')

