<h2>Serverless-A3</h2>
<p>The abstractive task in this assignment is to upload the text files on AWS S3 with delay of 100 ms using a script and trigger 1st Lambda function 'extractFeatures' as the files are uploaded. The lambda function will extract name entities and save in a Json file in another bucket. When file is uploaded on 2nd bucket, 2nd lambda function 'accessDB' will be triggered which will store the data to AWS RDS (MySQL database).
<p>All the code in the script and AWS lambda is Python 3.7 (tested). </p>
<p>After uploading all the files to AWS S3, I created lambda function using the help of the videos in the references. 'event' as an input in the lambda function is used to get the file name of the S3 bucket.</p>
<p>After fetching the bucket name, we get the key (object) of the bucket using boto3 module. It may throw an error because S3 may not have GetObject permission. We can generate a policy to allow GetObject and put it in the S3 permissions or add it in the IAM role created for the lambda function.<p>
<p>The logs shows that as soon as I upload a file, it is triggering a lambda function and all the content is being printed for now, Hence we can move further and extract named entities from them to store JSON file in another bucket.</p>
<p>To extract named entities, I need to use nltk python module, so I uploaded the module in the lambda file directory in a zip file. If the size is above 10 MB, then we must use AWS S3.</p>
<p> There were some packages we need to download for nltk like 'punkt', but downloading from default nltk directory is not possible here. Hence we define where to download and fetch it in the lambda function. After downloading it to the cwd, fetching it gives OS error as the package is only read only system. Hence we need to download the package in '/tmp' directory.</p>
<p>I created a dictionary from the tokenized words after removing stop words and stemming.</p>
<p>I created another python file 'S3APi' which contains functions to list the buckets and to upload a file to them. Now the task is to send the dictionary as JSON file to another bucket 'tagsb00845449'.</p>
<p>Before I was downloading and fetching the nltk packages from '/tmp' directory, but the problem is that it downloads the packages everytime the function is called which leads to request timeout (which is only 3 seconds) and whole function doesnt get executed. Hence I downloaded the nltk packages locally in nltk_data folder, uploaded to s3 bucket as a zip and created a layer from that. Then in the lambda function I specified the custom path to look for those path 'nltk.data.path.append('opt/nltk_data'). The reason I look in opt folder is that all the layer zip files are located in that directory. So this is a better solution.</p>
<p>As using lambda functions and installing additional packages doesnt seem easy on the website, I started using aws cli.</p>
<p>I updated the timeout and memory size of the function using cli command-> 'aws update-function-configuration --function-name extractFeatures --timeout'
<p>The lambda function is sending JSON file to another bucket. What we need to do now is trigger another lambda function on bucket 'tagsb00845449' when objects are created or uploaded. the lambda function will fetch the JSON file and save it to RDS MYSQL database.</p>
<p>A new lambda function is created which triggers tagsb00845449 bucket, fetches all the objects put in the bucket and extract entities from it. All these entities are stored with their respective frequencies in AWS RDS MYSQL database. If the entities are already present, the frequency is updated.</p>
<p>----->Finish<-----</p>
<h2> References </h2>
<p>https://www.youtube.com/watch?v=EsqjHDpLpB4</p>
<p>https://docs.aws.amazon.com/lambda/latest/dg/welcome.html</p>
<p>https://www.youtube.com/watch?v=vXiZO1c5Sk0</p>
<p>https://www.programcreek.com/python/example/91258/nltk.ne_chunk</p>
