import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY
logging.getLogger("pymongo").setLevel(logging.ERROR)

# load the certificate authority file to avoid timeout error when connecting to MongoDB
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is reponsible for establishing a connection to the MongoDB database.

    Attributes
    ----------
    client: MongoClient
        A shared MongoClient instance for the class.
    database: Database
        The specific database instance that MongoDBClient connects to.
         
    Methods
    -------
    __init__(database_name: str) -> None:
        Intializes the MongoDB connection using the given database name.
    """

    client = None # Shared MongoClient instance accross all MongoDBClient instance

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Parameters
        ----------
        database_name : str, optional
            Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.
        
        Raises
        ------
        Exception:
            If there is an issue connecting to MongoDB of if the environment variable for the MongoDB URL is not set.
        """
        try:
            # check if an MongoDB client connection has already been established; if not, create a new one
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
                
                # Establish a new MongoDB client connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            
            # Use the shared MongoClient for this instance
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful.")

        except Exception as e:
            # Raise a custom exception with traceback details if connection fails
            raise MyException(e, sys)