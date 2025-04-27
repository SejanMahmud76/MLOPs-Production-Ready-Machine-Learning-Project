import os
from pathlib import Path

project_name = "us_visa"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")





# for filepath in list_of_files:
#     # Wrap the filepath string in a Path object for convenient path methods
#     filepath = Path(filepath)
#
#     # Split the Path into directory part (filedir) and file name (filename)
#     filedir, filename = os.path.split(filepath)
#
#     # If the file should live in a subdirectory, ensure that directory exists
#     # exist_ok=True prevents an error if the directory already exists
#     if filedir != "":
#         os.makedirs(filedir, exist_ok=True)
#
#     # Check two conditions:
#     # 1. The file does not exist yet
#     # 2. The file exists but is empty (size == 0 bytes)
#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#         # Open the file in write mode:
#         # - Creates the file if it doesn't exist
#         # - Truncates it to zero length if it already exists
#         with open(filepath, "w") as f:
#             # No content is written; we just want an empty placeholder file
#             pass
#     else:
#         # If the file exists and contains data, skip creation and inform the user
#         print(f"file is already present at: {filepath}")