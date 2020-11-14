import csv
import os
import re
import shutil
import pandas as pd

current_path = os.getcwd()
delete_path = os.path.join(current_path, 'grades')

# Function to delete the folders if it exist do that replica is not made and we can everytime make a new folder.
def del_grades_folder():
    if os.path.isdir(delete_path):
        shutil.rmtree(delete_path)  #Use of shutill Library to delete the whole tree.
    #New Folder
    os.mkdir(delete_path)
