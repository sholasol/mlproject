import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_paths=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_paths, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_paths, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test to see if the file is logging

# if __name__=="__main__":
#     logging.info("logging has started")
