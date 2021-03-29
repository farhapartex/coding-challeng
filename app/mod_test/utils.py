import datetime
import time
from app import BASE_DIR


def check_request_timing():
    with open(BASE_DIR+"loggers.log") as log_file:
        file_data = log_file.readlines()
        last_line = file_data[-1].split(" - ")[0]
        last_request_time = last_line.split(",")[0]

        now = datetime.datetime.now()
        current_time = str(now).split(".")[0]

        if current_time == last_request_time:
            time.sleep(2)
