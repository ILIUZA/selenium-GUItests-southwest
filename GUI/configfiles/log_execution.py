import inspect
import logging
import os
from datetime import date
from pathlib import Path
from os import path


def logTestExecution(logLevel=logging.DEBUG):
    # A logger_name is the module that calls a logger
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # set level DEBUG by default
    logger.setLevel(logging.DEBUG)
    # create file handler and set level to logLevel (a parameter)
    # The logfile name is current_date.log
    # All the logfiles we save in a dir <logs>
    logfile_name = str(date.today()) + '.log'

    log_path1 = str(Path(__file__).resolve().parent.parent)
    log_path2 = '/logs/'

    log_path = log_path1 + log_path2
    logfile = log_path + logfile_name

    # If there isn't a dir <logs> we create it
    if not path.exists(log_path):
        os.mkdir(log_path)

    file_handler = logging.FileHandler(filename=logfile)
    file_handler.setLevel(logLevel)

    # create formatter. Append data in a log
    formatter = logging.Formatter('%(asctime)s | %(funcName)s | %(levelname)s |%(message)s')

    # add formatter
    file_handler.setFormatter(formatter)

    # add file_handler to logger
    logger.addHandler(file_handler)

    return logger
