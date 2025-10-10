from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger=get_logger(__name__)

def divide(a,b):
    try:
        result=a/b
        logger.info("dividing two numbers")
        return result
    except Exception as e:
        logger.error("Error occured")
        raise CustomException("Custom Error zero",sys)
    
if __name__=="__main__":
    try:
        logger.info("Starting")
        divide(10,2)
    except CustomException as ce:
        logger.error(str(ce))