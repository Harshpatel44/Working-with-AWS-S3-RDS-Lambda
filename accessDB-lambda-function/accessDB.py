import json
import RdsApi
import boto3
def lambda_handler(event, context):
    s3=boto3.client('s3')
    if(event):
        event_object = event["Records"][0]
        file_name = str(event_object["s3"]["object"]["key"])
        file_object=s3.get_object(Bucket='tagsb00845449',Key=file_name)
        content = file_object["Body"].read().decode('utf-8')
        content=json.loads(content)
        dictionary = content[file_name.split('.')[0]]
        print(dictionary)
        api = RdsApi()
        for i in dictionary.keys():
            current_frequency=api.checkNameExist(i)
            if(current_frequency==0):
                api.addData(i,dictionary[i])
            else:
                api.updateName(i,current_frequency+dictionary[i])
        print('table updated for object {0}'.format(file_name))
