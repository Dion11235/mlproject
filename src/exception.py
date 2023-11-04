import sys
from logger import logging
# import logging

def error_handler(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    
    error_msg = f"Error occured in the file {file_name} in line {line_no}. Error message : {str(error)}"
    
    return error_msg
    
class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_handler(error=error_msg, error_detail=error_detail)
        
    def __str__(self):
        return self.error_msg
    
    
if __name__ == "__main__":
    
    # try:
    #     # Simulate an exception
    #     x = 1 / 0
    # except CustomException as e:
    #     print(f"Caught a custom exception: {e}")
    try:
        a = 1/0
    except Exception as e:
        print(f"Caught an exception : {CustomException(e, sys)}")
        logging.info(str(e))