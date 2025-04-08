from sensor.exception import SensorException
import os
import sys

from sensor.logger import logging

def test_exception():
    try:
        logging.info("An error is occured if division by zero")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)   # or (raise e)



if __name__ == "__main__":             #module execution control
    try:
        test_exception()
    except Exception as e:
        print(e)