#File is used to design the folder structure and record all the basic things
#.github folder is used for CI CD deplyment
import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')
project_name='text_summarizer'

list_of_files=[".github/workflows/.gitkeep",f"src/{project_name}/__init__.py",f"src/{project_name}/components/__init__.py",f"src/{project_name}/utils/__init__.py",f"src/{project_name}/components/common.py",f"src/{project_name}/logging/__init__.py",f"src/{project_name}/config/__init__.py",f"src/{project_name}/config/configuration.py",f"src/{project_name}/pipeline/__init__.py",f"src/{project_name}/entity/__init__.py",f"src/{project_name}/constants/__init__.py","config/config.yaml","params.yaml","app.py","main.py","Dockerfile","requirements.txt","setup.py","research/trails.ipynb"]

for filepath in list_of_files:
    f_path=Path(filepath)
    folder,file=os.path.split(f_path)
    # check folder name is blank or not, folder only will be created only if name is not blank
    if folder !="":
        os.makedirs(folder,exist_ok=True)
        logging.info(f"Creating Directory {folder}")
    else:
        logging.info("Folder name is blank")
    #now creating files inside folder
    #checking two conditions 1. first if the file does not exists 2. if the size of existing file is 0
    if not os.path.exists(filepath) or os.path.getsize(filepath)==0:
        with open(filepath ,'w') as f:
            pass
            logging.info(f"Creating {file} inside {folder}")
    else:
        logging.info(f"{file} already exists")

