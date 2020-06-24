<h2>Serverless-A3</h2>
<p>The abstractive task in this assignment is to upload the text files on AWS S3 with delay of 100 ms using a script and trigger 1st Lambda function 'extractFeatures' as the files are uploaded. The lambda function will extract name entities and save in a Json file in another bucket. When file is uploaded on 2nd bucket, 2nd lambda function 'accessDB' will be triggered which will store the data to AWS RDS (MySQL database).
<p>All the code in the script and AWS lambda is Python 3.7 (tested). </p>
<p>After uploading all the files to AWS S3, I created lambda function using the help of the videos in the references. 'event' as an input in the lambda function is used to get the file name of the S3 bucket.</p>
<p>After fetching the bucket name, we get the key (object) of the bucket using boto3 module. It may throw an error because S3 may not have GetObject permission. We can generate a policy to allow GetObject and put it in the S3 permissions or add it in the IAM role created for the lambda function.<p>
<p>The logs shows that as soon as I upload a file, it is triggering a lambda function and all the content is being printed for now, Hence we can move further and extract named entities from them to store JSON file in another bucket.</p>
<p>To extract named entities, I need to use nltk python module, so I uploaded the module in the lambda file directory in a zip file. If the size is above 10 MB, then we must use AWS S3.</p>
<p> There were some packages we need to download for nltk like 'punkt', but downloading from default nltk directory is not possible here. Hence we define where to download and fetch it in the lambda function. After downloading it to the cwd, fetching it gives OS error as the package is only read only system. Hence we need to download the package in '/tmp' directory.</p>
<p>I created a dictionary from the tokenized words after removing stop words and stemming.</p>
  
<h2> References </h2>
<p>https://www.youtube.com/watch?v=EsqjHDpLpB4</p>
<p>https://docs.aws.amazon.com/lambda/latest/dg/welcome.html</p>
<p>https://www.youtube.com/watch?v=vXiZO1c5Sk0</p>
