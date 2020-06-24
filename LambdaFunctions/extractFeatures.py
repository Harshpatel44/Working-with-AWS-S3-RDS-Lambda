import boto3
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

from LambdaFunctions import S3Api


def extractFeatures(event,context):
    s3 = boto3.client('s3')
    if(event):
        event_object = event["Records"][0]
        file_name = str(event_object["s3"]["object"]["key"])
        file_object = s3.get_object(Bucket = 'sample-data-b00845449',Key = file_name)
        content = file_object["Body"].read().decode('utf-8')

        ps = PorterStemmer()
        dictionary = {}
        words = word_tokenize(content)
        stop_words = set(stopwords.words("english"))
        for i in words:
            if (i not in stop_words):
                if (ps.stem(i) in dictionary):
                    dictionary[ps.stem(i)] += 1
                else:
                    dictionary[ps.stem(i)] = 1
        print(dictionary)

        s3 = S3Api.s3Api()
        s3.sendJSONObject("tagsb00845449", file_name, {str(file_name.split('.')[0]) + 'ne': dictionary})