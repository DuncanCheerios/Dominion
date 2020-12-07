from datetime import datetime
import time
from os import path, makedirs

GAME_LOGS_PATH = "game_logs/"
TIME_FORMAT = "%Y%m%dT%H%M%S"
PRETTY_TIME_FORMAT = "%m/%d/%Y  %I:%M %p"
class game_logger():

    def __init__(self):
        
        # Create a new log in the log folder for the new game
        self._filepath = f"{GAME_LOGS_PATH}log_{datetime.now().strftime(TIME_FORMAT)}.txt"

        # Create folder (if it does not exist)
        if not path.exists(path.dirname(self._filepath)):
            try:
                makedirs(path.dirname(self._filepath))
            except OSError:
                raise
        with open(self._filepath, "w") as logfile:
            logfile.write(f"Game Started at {datetime.now().strftime(PRETTY_TIME_FORMAT)}\n")


    def log(self, stuff):
        with open(self._filepath, "a") as logfile:
            logfile.write(stuff)
            logfile.write("\n")


    def log_lines(self, line_list):
        with open(self._filepath, "a") as logfile:
            for line in line_list:
                logfile.write(line + "\n")



if __name__=="__main__":
    logger = game_logger()
    logger.log("HELLO WORLD")
    lines = ["First Line", "Second Line", "Third Line"]
    logger.log_lines(lines)