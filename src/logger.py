import logging
import os
from datetime import datetime


log_dir_path = os.path.join(os.getcwd(), "Logs")
os.makedirs(log_dir_path, exist_ok=True)

# log_file_name = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
# log_file_name = f"dummy.log"
log_file_name = f"{datetime.now().strftime('%d-%m-%Y')}.log"

log_file_path = os.path.join(log_dir_path, log_file_name)

logging.basicConfig(
    filename = log_file_path,
    format = "[ %(asctime)s ] %(name)s %(lineno)d - %(levelname)s - %(message)s",
    level = logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")
