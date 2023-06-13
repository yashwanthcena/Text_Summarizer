import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: [%(message)s]:')


PROJECT_NAME = 'TextSummarizer'

list_of_files =[
    "./github/workflows/gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/utlis/__init.py"
    f"src/{PROJECT_NAME}/utlis/common.py"
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py"
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py"
    "params.py",
    "config/configuration.py",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename =  os.path.split(filepath)

    if filedir!= "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"created new :{filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , 'w') as f:
            pass
        logging.info(f"creating empty file : {filepath}")

    else:

        logging.info(f"{filepath} already exists")

        

