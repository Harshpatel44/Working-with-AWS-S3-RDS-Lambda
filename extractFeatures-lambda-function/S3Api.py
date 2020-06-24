import boto3
class s3Api:
    """ Get name of the buckets """
    def listBuckets(self):
        s3 = boto3.client('s3')
        return s3.list_buckets()

    """ Send content to bucket object """
    def sendJSONObject(self, bucket_name, source_file_name, content):
        s3Resource = boto3.resource('s3')
        s3Resource.Object(bucket_name, source_file_name).put(Body=(bytes(json.dumps(content).encode('UTF-8'))))
        print('file uploaded')