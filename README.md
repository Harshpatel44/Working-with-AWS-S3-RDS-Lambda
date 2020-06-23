<h2>Serverless-A3</h2>
<p>The abstractive task in this assignment is to upload the text files on AWS S3 with delay of 100 ms using a script and trigger 1st Lambda function 'extractFeatures' as the files are uploaded. The lambda function will extract name entities and save in a Json file in another bucket. When file is uploaded on 2nd bucket, 2nd lambda function 'accessDB' will be triggered which will store the data to AWS RDS (MySQL database).

<p> All the code in the script and AWS lambda is Python 3.7 (tested). </p>

<h2> References </h2>
<p>https://www.youtube.com/watch?v=EsqjHDpLpB4</p>
<p>https://docs.aws.amazon.com/lambda/latest/dg/welcome.html</p>
<p>https://www.youtube.com/watch?v=vXiZO1c5Sk0</p>
