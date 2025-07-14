import json
import os
import sys
import subprocess
import shutil
import os
import logging

logging.basicConfig(level = logging.INFO)

DB_NAME = sys.argv[1] 
DB_USER = sys.argv[2] 
DB_PASSWORD = sys.argv[3]
NS= sys.argv[4]
PORT= sys.argv[5]
# Df Pipelines
directory = "IE/DataFusion/Pipeline"

# specify the old and new string pairs you want to replace
replace_dict = {
    "ENV_CLOUD_SQL_DB_NAME": DB_NAME,
    "ENV_CLOUD_SQL_USER_NAME": DB_USER,
    "ENV_CLOUD_SQL_PASSWORD": DB_PASSWORD,
    "ENV_PORT": PORT
}

# loop through all files in the directory
for filename in os.listdir(directory):

    if filename.endswith(".json"): # replace only in .json files (you can change this condition as per your requirement)
        # read the file contents
        with open(os.path.join(directory, filename), 'r') as file:
            file_contents = file.read()
        
        # replace all old strings with their respective new strings
        for old_str, new_str in replace_dict.items():
            file_contents = file_contents.replace(old_str, new_str)
        
        try:
            # write the updated contents back to the file
            with open(os.path.join(directory, filename), 'w') as file:
                file.write(file_contents)
            logging.info(f"File {filename} updated")
        except Exception as e:
            logging.error(f"Error updating file {filename}")

#Call the migrate script
os.chdir('IE/DataFusion')
migrate= "./migrate.sh"
os.chmod(migrate,0o755)
subprocess.call([migrate,NS])
