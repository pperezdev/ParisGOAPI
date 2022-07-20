import boto3
from botocore.exceptions import ClientError
import datetime
import io
import os
import uuid

from dotenv import load_dotenv
load_dotenv()

class s3Insert:
    def __init__(self):
        self.s3_client = boto3.client('s3', 
                region_name='us-east-1', 
                aws_access_key_id=os.getenv("ACCESS_KEY"),
                aws_secret_access_key=os.getenv("ACCESS_SECRET"))


    def upload_my_file(self, bucket, folder, file_as_binary, file_name):
            file_as_binary = io.BytesIO(file_as_binary)
            key = folder+"/"+file_name
            try:
                self.s3_client.upload_fileobj(file_as_binary, bucket, key)
            except ClientError as e:
                print(e)
                return False
            return True