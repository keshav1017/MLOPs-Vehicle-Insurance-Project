import boto3
import os
from src.constants import AWS_ACCESS_ID_ENV_KEY, AWS_SECRET_ACCESS_KEY_ENV_KEY, REGION_NAME

import logging

logging.getLogger("boto3").setLevel(logging.WARNING)
logging.getLogger("botocore").setLevel(logging.WARNING)

class S3Client:
    s3_client = None
    s3_resource = None
    def __init__(self, region_name = REGION_NAME):
        """
        This class gets aws credentials from env_variable and creates a connection with s3 bucket 
        and raises an exception when environment variables are not set.
        """

        if S3Client.s3_client == None or S3Client.s3_resource == None:
            __access_key_id = os.getenv(AWS_ACCESS_ID_ENV_KEY)
            __secret_access_key_id = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

            if __access_key_id is None:
                raise Exception(f"Environment variable: {AWS_ACCESS_ID_ENV_KEY} is not set.")
            if __secret_access_key_id is None:
                raise Exception(f"Environment variable: {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set.")
            
            S3Client.s3_resource = boto3.resource('s3',
                                                  aws_access_key_id=__access_key_id,
                                                  aws_secret_access_key=__secret_access_key_id,
                                                  region_name=region_name)
            S3Client.s3_client = boto3.client('s3',
                                              aws_access_key_id=__access_key_id,
                                              aws_secret_access_key=__secret_access_key_id,
                                              region_name=region_name)
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client