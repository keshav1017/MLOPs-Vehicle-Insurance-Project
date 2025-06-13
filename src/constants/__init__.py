import os 
from datetime import date

# For MongoDB connection
DATABASE_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"
MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "Response"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME = "data.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

AWS_ACCESS_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

"""
Data Ingestion related constants start with DATA_INGESTION VAR NAME.
"""

DATA_INGESTION_COLLECTION_NAME = "Proj1-Data"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.25

"""
Data Validation related constants start with DATA_VALIDATION VAR NAME.
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

"""
Data Transformation related constant start with DATA_TRANSFORMATION VAL NAME.
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

"""
Model Trainer related constants start with MODEL_TRAINER VAR NAME.
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS = 200
MODEL_TRAINER_MIN_SAMPLES_SPLIT = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF = 6
MIN_SAMPLES_SPLIT_MAX_DEPTH = 10
MIN_SAMPLES_SPLIT_CRITERION = 'entropy'
MIN_SAMPLES_SPLIT_RANDOM_STATE = 101

"""
Model Evaluation related constants
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "vehi-insu-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"

APP_HOST = "0.0.0.0"
APP_PORT = 5000