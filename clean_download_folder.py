import os
import shutil
from datetime import datetime, timedelta

# Set the directory path to the Downloads folder
folder_path = os.path.join(os.path.expanduser("~"), "Downloads")

# set the directory path to the 30_days_old folder
old_files_path = os.path.join(folder_path, "30_days_old")

# create the 30_Days_Old folder if it doesn't exist
if not os.path.exists(old_files_path):
    os.mkdir(old_files_path)

# get the list of files in the folder
files = os.listdir(folder_path)

# get the current date
now = datetime.now()

# loop through the files
for file in files:
    # get the file path
    file_path = os.path.join(folder_path, file)

    # get the file's modified date
    modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))

    # calculate the time difference
    time_difference = now - modified_date

    # if the file is older than 30 days, move it
    if time_difference > timedelta(days=30):
        shutil.move(file_path, old_files_path)
