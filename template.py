import os 
from pathlib import Path
import logging

list_of_files = [
    
    # folder for github actions
    ".github/worflows/.gitkeep",
    "src/__init__.py",
    # for all stages of ml pipeline (training and inferencing pipeline)
    "src/components__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py"
    # pipeline folder
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py"
    # folder for utilities
    "src/utils/__init__.py"
    "src/utils/utils.py",
    # folder for logger 
    "src/logger/logging.py",
    # folder for exception
    "src/exception/exception.py"
    # folder for testing of code
    "test/uint/__init__.py", # unit testing single unit 
    "test/integration/__init__.py" # integration for testing all units in one shot
    "init_setup.sh",
    "requirements.txt",
    ".gitignore",
    "requirements_dev.txt", # for dev enviorment for production all requirements will be here
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: _{filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass