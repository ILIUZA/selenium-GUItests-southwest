import os
from pathlib import Path
from os import path
from time import strftime, localtime


# Take screenshot and save it a dir <screenshots> with extension .png
def screenshotIt(driver):
    log_path1 = str(Path(__file__).resolve().parent.parent)
    log_path2 = '/screenshots/'
    log_path3 = strftime("%Y-%m-%d-%H-%M-%S", localtime()) + '.png'
    logfile = log_path1 + log_path2 + log_path3
    # if a dir doesn't exist create it
    if not path.exists(log_path1 + log_path2):
        os.mkdir(log_path1 + log_path2)

    driver.save_screenshot(logfile)


