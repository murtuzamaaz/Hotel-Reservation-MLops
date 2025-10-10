import os 
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml    

logger=get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config=config["data_ingestion"]
        self.bucket_name=self.config["bucket_name"]
        self.file_name=self.config["bucket_file_name"]
        self.train_test_ratio=self.config["train_ratio"]

        os.makedirs(RAW_DIR,exist_ok=True)
        logger.info(f"Data ingestion started with {self.bucket_name} and file name {self.file_name} ")

    def download_csv_from_gcp(self):
        try:
            client=storage.Client()
            bucket=client.bucket(self.bucket_name)
            blob=bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"raw file is sucessfully downloaded to {RAW_FILE_PATH}")
        except Exception as e:
            logger.error("Error while downloading the file from GCP Failed to download the csv")
            raise CustomException("Error in downloading",e)
    def split_data(self):
        try:
            logger.info("splititin the dataset is started")
            data=pd.read_csv(RAW_FILE_PATH)

            train_data,test_data=train_test_split(data,test_size=1-self.train_test_ratio,random_state=42)
            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)
            logger.info(f"train and test file is created at {TRAIN_FILE_PATH}")
            logger.info(f"train and test file is created at {TEST_FILE_PATH}")

        except Exception as e:
            logger.error("Error while splitting the data")
            raise CustomException("Failed to split the data in train and test",e)
    
    def run(self):
        try:
            logger.info("Data ingestion is started")

            self.download_csv_from_gcp()
            self.split_data()

            logger.info("Data ingestion is completed suceesfullt")
        except Exception as e:
            logger.error("Error in the run method of data ingestion")
            raise CustomException(f"Custom exception occured in the run method of data ingestion ",e)
        finally:
            logger.info("Data ingestion is completed")
        


if __name__=="__main__":
    dataIngestion=DataIngestion(read_yaml(CONFIG_PATH))
    dataIngestion.run()

