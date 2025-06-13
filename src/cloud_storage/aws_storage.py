import boto3
from io import StringIO
from typing import Union, List
from mypy_boto3_s3.service_resource import Bucket
from botocore.exceptions import ClientError
from pandas import DataFrame, read_csv
import os, sys
import pickle

from src.logger import logging
from src.configuration.aws_connection import S3Client
from src.exception import MyException

class SimpleStorageService:
    """
    A class for interacting with AWS S3 storage, providing for file management,
    data uploads, and data retrieval in S3 bucket.
    """

    def __init__(self):
        """
        Initializes SimpleStorage class instance with S3 resource and client 
        from S3Client Class.
        """
        s3_client = S3Client()
        self.s3_resource = s3_client.s3_resource
        self.s3_client = s3_client.s3_client
    
    def s3_key_path_available(self, bucket_name: str, s3_key: str) -> bool:
        """
        Checks if a specified S3 key path (file path) is available in the specified bucket.

        Args:
            bucket_name (str): Name of the s3 bucket.
            s3_key (str): Key path of the file to check.
        Returns:
            bool: True if the file exists.
        """
        try:
            bucket = self.get_bucket(bucket_name)
            file_objects = [file_object for file_object in bucket.objects.filter(Prefix=s3_key)]
            return len(file_objects) > 0
        except Exception as e:
            raise MyException(e, sys)
    
    @staticmethod
    def read_object(object_name: str, decode: bool, make_readable: bool = False) -> Union[StringIO, str]:
        """ 
        Reads the specified S3 object with optional decoding and formatting.

        Args:
            object_name: The S3 object name.
            decode : Whether to decode the object content as a string.
            make_readable: Whether to convert content to StringIO for DataFrame usage.
        """
        try:
            # read and decode the object if decode is True
            func = (
                lambda: object_name.get()["Body"].read().decode()
                if decode else object_name.get()["Body"].read()
            )
            # convert to StringIO if make_readable=True
            conv_func = lambda: StringIO(func()) if make_readable else func()
            return conv_func()
        except Exception as e:
            raise MyException(e, sys)
    
    def get_bucket(self, bucket_name: str) -> Bucket:
        """
        Retrieves the S3 bucket object based on the provided bucket name.

        Args:
            bucket_name: The name of the S3 bucket.
        
        Returns:
            Bucket: S3 bucket object
        """
        logging.info("Entered the get_bucket method of SimpleStorageService class")
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            logging.info("Exited the get_bucket method of SimpleStorageService class")
            return bucket
        except Exception as e:
            raise MyException(e, sys)
        
    def get_file_object(self, filename: str, bucket_name: str) -> Union[List[object], object]:
        """
        Retrieves the file object(s) from the specified bucket based on the filename.e

        Args:
            filename: The name of the file to retrieve
            bucket_name: The name of the S3 bucket
        
        Returns:
            Union[List[object], object]: The S3 file object or list of file objects.
        """
        logging.info("Entered the get_file_object method of SimpleStorageService Class")
        try:
            bucket = self.get_bucket(bucket_name)
            file_objects = [file_object for file_object in bucket.objects.filter(Prefix=filename)]
            func = lambda x: x[0] if len(x) == 1 else x
            file_objs = func(file_objects)
            logging.info("Exited the get_file_objects method of SimpleStorageService class")
            return file_objs
        except Exception as e:
            raise MyException(e, sys)
    
    def load_model(self, model_name: str, bucket_name: str, model_dir: str = None) -> object:
        """
        Loads a serialized model from specified S3 bucket.

        Args:
            model_name: Name of the model file in the bucket.
            bucket_name: Name of the S3 bucket.
            model_dir: Directory path within the bucket.
        
        Returns:
            objects: The decentralized model objects.
        """
        try:
            model_file = model_dir + "/" + model_name if model_dir else model_name
            file_object = self.get_file_object(model_file, bucket_name)
            model_obj = self.read_object(file_object, decode=False)
            model = pickle.loads(model_obj)
            logging.info("Production model loaded from S3 bucket")
            return model
        except Exception as e:
            raise MyException(e, sys)
        
    def create_folder(self, folder_name: str, bucket_name: str) -> None:
        """
        Creates a folder in the specified S3 bucket.

        Args:
            folder_name: Name of the folder to create.
            bucket_name: Name of the S3 bucket.
        """
        logging.info("Entered the create_folder method of SimpleStorageService class")
        try:
            # check if the folder already exists attempting to load it
            self.s3_resource.Object(bucket_name, folder_name).load()
        except ClientError as e:
            # if not created then create it
            if e.response["Error"]["Code"] == "404":
                folder_obj = folder_name + "/"
                self.s3_client.put_object(Bucket=bucket_name, Key=folder_obj)
            logging.info("Exited the create_folder method of SimpleStorageService class")
    
    def upload_file(self, from_filename: str, to_filename: str, bucket_name: str, remove: bool = True):
        """
        Uploads a local file to the specified S3 bucket with an optional file deletion.

        Args:
            from_filename: Path of the local file
            to_filename: Target file path in the bucket
            bucket_name: Name of the S3 bucket
            remove: if True, deletes the local file after upload.
        """
        logging.info("Entered the upload_file method of SimpleStorageService class")
        try:
            logging.info(f"Uploading {from_filename} to {to_filename} in {bucket_name}")
            self.s3_resource.meta.client.upload_file(from_filename, bucket_name, to_filename)
            logging.info("Uploaded {from_filename} to {to_filename} in {bucket_name}")

            # delete the local file if remove is True
            if remove:
                os.remove(from_filename)
                logging.info(f"Removed local file {from_filename} after upload.")
            logging.info("Exited the upload_file method of SimpleStorageService class")
        except Exception as e:
            raise MyException(e, sys) from e
    
    def upload_df_as_csv(self, data_frame: DataFrame, local_filename: str, bucket_filename: str, bucket_name: str) -> None:
        """
        Uploads a Dataframe as a CSV file to the specified S3 bucket.

        Args:
            data_frame: Dataframe to be uploaded
            local_filename: Temporary local filename for the Dataframe
            bucket_filename: Target filename in the bucket
            bucket_name: Name of the S3 bucket.
        """
        logging.info("Entered the upload_df_as_csv method of SimpleStorageService class")
        try:
            # Save DataFrame to CSV locally and then upload it
            data_frame.to_csv(local_filename, index=None, header=True)
            self.upload_file(local_filename, bucket_filename, bucket_name)
            logging.info("Exited the upload_df_as_csv method of SimpleStorageService class")
        except Exception as e:
            raise MyException(e, sys) from e
    
    def get_df_from_object(self, object_: object) -> DataFrame:
        """
        Converts an S3 object to a Dataframe.

        Args:
            object_: The S3 object.
        
        Returns:
            DataFrame: DataFrame created from the object content.
        """
        logging.info("Entered the get_df_from_object method of SimpleStorageService class.")
        try:
            content = self.read_object(object_, make_readable=True)
            df = read_csv(content, na_values="na")
            logging.info("Exited the get_df_from_object method of SimpleStorageService class")
            return df
        except Exception as e:
            raise MyException(e, sys) from e
    
    def read_csv(self, filename: str, bucket_name: str) -> DataFrame:
        """
        Reads a CSV file from the specified S3 bucket and converts it to a DataFrame.

        Args:
            filename: The name of the file in the bucket.
            bucket_name: The name of the S3 bucket.
        
        Returns:
            DataFrame: DataFrame created from the CSV file.
        """
        logging.info("Entered the read_csv method of SimpleStorageService class")
        try:
            csv_obj = self.get_file_object(filename, bucket_name)
            df = self.get_df_from_object(csv_obj)
            logging.info("Exited from the read_csv method of SimpleStorageService class")
            return df
        except Exception as e:
            raise MyException(e, sys) from e