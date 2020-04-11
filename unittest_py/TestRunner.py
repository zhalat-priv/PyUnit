import os
from utils.log import get_logger
from utils.fileLog import Logs 

log_console = get_logger()
log_file = Logs("TestRunnerLog.txt")

if __name__ == '__main__':
    log_console.info("TestRunner start")
    log_file.write("TestRunner start")