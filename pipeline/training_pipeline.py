from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataPreprocessor
from src.model_trainig import ModelTraining
from utils.common_functions import read_yaml
from config.paths_config import *
from config.model_params import *



if __name__=='__main__':
    #### DATA Ingestion #######
    dataIngestion=DataIngestion(read_yaml(CONFIG_PATH))
    dataIngestion.run()

    ####### Data Processing ########
    processor=DataPreprocessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)

    processor.process()

    ##### Training ######
    trainer=ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUPUT_PATH)
    trainer.run()

    







