import sys
import os
from src.entity.config_entity import VehiclePredictConfig
from src.utils.main_utils import load_object
from src.exception import MyException
from src.logger import logging
from pandas import DataFrame

class VehicleData:
    def __init__(self,
                 Gender,
                 Age,
                 Driving_License,
                 Region_Code,
                 Previously_Insured,
                 Annual_Premium,
                 Policy_Sales_Channel,
                 Vintage,
                 Vehicle_Age_lt_1_Year,
                 Vehicle_Age_gt_2_Years,
                 Vehicle_Damage_Yes):
        """
        Vehicle Data constructor
        Input: all feature of the trained model prediction
        """
        try:
            self.Gender = Gender
            self.Age = Age
            self.Driving_License = Driving_License
            self.Region_Code = Region_Code
            self.Previously_Insured = Previously_Insured
            self.Annual_Premium = Annual_Premium
            self.Policy_Sales_Channel = Policy_Sales_Channel
            self.Vintage = Vintage
            self.Vehicle_Age_lt_1_Year = Vehicle_Age_lt_1_Year
            self.Vehicle_Age_gt_2_Years = Vehicle_Age_gt_2_Years
            self.Vehicle_Damage_Yes = Vehicle_Damage_Yes
        
        except Exception as e:
            raise MyException(e, sys) from e
    
    def get_vehicle_data_dataframe(self):
        """
        This function returns a dataframe from VehicleData class input.
        """

        try:
            vehicle_data_input = self.get_vehicle_data_as_dict()
            return DataFrame(vehicle_data_input)
        except Exception as e:
            raise MyException(e, sys) from e

    def get_vehicle_data_as_dict(self) -> DataFrame:
        """
        This function returns a dictionary from VehicleData class input
        """
        logging.info("Entered get_vehicle_data_as_dict method of VehicleData class")
        try:
            input_data = {
                "Gender": [self.Gender],
                "Age": [self.Age],
                "Driving_License": [self.Driving_License],
                "Region_Code": [self.Region_Code],
                "Previously_Insured": [self.Previously_Insured],
                "Annual_Premium": [self.Annual_Premium],
                "Policy_Sales_Channel": [self.Policy_Sales_Channel],
                "Vintage": [self.Vintage],
                "Vehicle_Age_lt_1_Year": [self.Vehicle_Age_lt_1_Year],
                "Vehicle_Age_gt_2_Years": [self.Vehicle_Age_gt_2_Years],
                "Vehicle_Damage_Yes": [self.Vehicle_Damage_Yes]
            }

            logging.info("Created vehicle data dict")
            logging.info("Exited get_vehicle_data_as_dict method of VehicleData class")
            return input_data
        except Exception as e:
            raise MyException(e, sys) from e
    
class VehicleDataClassifier:
    def __init__(self, prediction_pipeline_config: VehiclePredictConfig = VehiclePredictConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise MyException(e, sys)
    
    def get_latest_model_path(self, artifact_dir="artifact", model_subpath=os.path.join("model_trainer", "model_trainer", "model.pkl")):
        # List all timestamped subdirectories in artifact/
        subdirs = [os.path.join(artifact_dir, d) for d in os.listdir(artifact_dir)
                if os.path.isdir(os.path.join(artifact_dir, d))]
        if not subdirs:
            raise FileNotFoundError("No timestamp folders found in artifact/")
        # Sort by modification time, descending
        latest_subdir = max(subdirs, key=os.path.getmtime)
        model_path = os.path.join(latest_subdir, model_subpath)
        # print(model_path)
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        return model_path

    def predict(self, dataframe) -> str:
        """
        This is method of VehicleDataClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of VehicleDataClassifier")
            latest_model_path = self.get_latest_model_path()
            model = load_object(latest_model_path)
            result = model.predict(dataframe)

            return result
        except Exception as e:
            raise MyException(e, sys)