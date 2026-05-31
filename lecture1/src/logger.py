import logging

# for logging information into txt file

import os
from datetime import datetime

LOG_File=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#in above naming covention file will be created i.e month date..)
logs_path=os.path.join(os.getcwd(),"logs",LOG_File) #logs will be created in working current dir
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_File)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")


# after running it creates a logs folder and it has 
#[2026-05-30 22:44:17,473] 22 root -INFO -Logging has started
