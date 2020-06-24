import json
import boto3
import RdsApi

def lambda_handler(event=1, context=1):
    s3=boto3.client('s3')
    file_name='450.txt'
    file_object=s3.get_object(Bucket='tagsb00845449',Key=file_name)
    content = file_object["Body"].read().decode('utf-8')
    content=json.loads(content)
    dictionary = content[file_name.split('.')[0]+'ne']
    dictionary={'harsh':2}


    api = RdsApi()
    for i in dictionary.keys():
        current_frequency=api.checkNameExist('harsh')
        if(current_frequency==0):
            api.addData(i,dictionary[i])
        else:
            api.updateName(i,current_frequency+dictionary[i])
    print('finish')
lambda_handler()
