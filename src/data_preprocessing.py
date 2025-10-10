import os 
import pandas as pd
import numpy as np
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml,load_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

logger=get_logger(__name__)

class DataPreprocessor:
    def __init__(self,train_path,test_path,processed_dir,config_path):
        self.train_path=train_path
        self.test_path=test_path
        self.processed_dir=processed_dir

        self.config=read_yaml(config_path)

        if not os.path.exists(self.processed_dir):
            os.makedirs(self.processed_dir)
            logger.info(f"Created directory: {self.processed_dir}")

    def preprocess_data(self,df):
        try:
            logger.info("Starting data preprocessing")

            logger.info("Dropping the columns")

            df.drop(columns=['Unnamed: 0','Booking_ID'],inplace=True)
            df.drop_duplicates(inplace=True)
            cat_cols=self.config['data_processing']['categorical_columns']
            num_cols=self.config['data_processing']['numerical_columns']

            logger.info("Encoding categorical columns using Label Encoding")

            le=LabelEncoder()

            mappings={}

            for col in cat_cols:
                df[col]=le.fit_transform(df[col])
                mappings[col]={label:code for label,code in zip(le.classes_,le.transform(le.classes_))}
            
            logger.info('Label Mappings are:')
            for col, mapping in mappings.items():
                logger.info(f"{col}: {mapping}")
            
            logger.info('Handling skewness in numerical columns using log1p transformation')

            skew_threshold=self.config['data_processing']['skewness_threshold']

            skewness=df[num_cols].apply(lambda x:x.skew())
            for column in skewness[skewness>skew_threshold].index:
                df[column]=np.log1p(df[column])

            return df
        except Exception as e:
            logger.error(f"Error in data preprocessing: {e}")
            raise CustomException("Error during the data preprocessing",e)
        
    def balance_data(self,df):
        try:
            logger.info("Balancing the dataset using SMOTE")

            X=df.drop(columns=['booking_status'])
            y=df['booking_status']
            smote=SMOTE(random_state=42)
            X_resampled,y_resampled=smote.fit_resample(X,y)

            balanced_df=pd.DataFrame(X_resampled,columns=X.columns)
            balanced_df['booking_status']=y_resampled

            logger.info("Successfully balanced the dataset")
            return balanced_df
        except Exception as e:
            logger.error(f"Error in balancing the dataset: {e}")
            raise CustomException("Error during the data balancing",e)
    
    def select_features(self,df):
        try:
            logger.info("Selecting important features using Random Forest Classifier")

            X=df.drop(columns=['booking_status'])
            y=df['booking_status']

            model=RandomForestClassifier(random_state=42)
            model.fit(X,y)

            feature_importances=model.feature_importances_

            feature_importance_df=pd.DataFrame({
                    'feature':X.columns,
                    'importance':feature_importances
                }
            )

            top_feature_importance_df=feature_importance_df.sort_values(by='importance',ascending=False)
            num_of_features_to_select=self.config['data_processing']['no_of_features']

            top_10_feature=top_feature_importance_df['feature'].head(num_of_features_to_select).values

            logger.info(f"Features Selectd: {top_10_feature}")

            top_10_df=df[top_10_feature.tolist()+['booking_status']]

            logger.info(f"Feature selection completed sucessfully")

            return top_10_df
        except Exception as e:  
            logger.error(f"Error in feature selection: {e}")
            raise CustomException("Error during the feature selection process",e)

    def save_data(self,df,file_path):
        try:
            logger.info("Saving proceseed data in csv in processed folder")

            df.to_csv(file_path,index=False)

            logger.info(f"Processed data saved at: {file_path}")

        except Exception as e:
            logger.error(f"Error in saving processed data: {e}")
            raise CustomException("Error during the data saving process",e)
        
    def process(self):
        try:
            logger.info("Loading data from Raw directory")

            train_df=load_data(self.train_path)
            test_df=load_data(self.test_path)

            train_df=self.preprocess_data(train_df)
            test_df=self.preprocess_data(test_df)

            train_df=self.balance_data(train_df)
            test_df=self.balance_data(test_df)

            train_df=self.select_features(train_df)
            test_df=test_df[train_df.columns]

            self.save_data(train_df,PROCESSED_TRAIN_DATA_PATH)
            self.save_data(test_df,PROCESSED_TEST_DATA_PATH)
        except Exception as e:
            logger.error(f"Error in the data pre processing pipeline: {e}")
            raise CustomException("Error during the data pre processing pipeline",e)
        


if __name__=="__main__":
    processor=DataPreprocessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)

    processor.process()







