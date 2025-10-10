import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger=get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file is not in the given path")
        with open(file_path,"r") as yaml_files:
            config=yaml.safe_load(yaml_files)
            logger.info("Sucessfully read the YAML file")
            return config
        
    
    except Exception as e:
        logger.error("Error while reading yaml file")
        raise CustomException("Failed to read file {e}")
    
    
def load_data(path):
    try:
        logger.info(f"Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error("Error while loading the data {e}")
        raise CustomException(f"Failed to load data ",e)
