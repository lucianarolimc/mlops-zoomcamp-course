## List of commands used in the development process

```bash

# create the conda environment
conda create -n mlops_zoomcamp python=3.10.16

# activate the environment
conda activate mlops_zoomcamp

# install the requirements
pip install -r requirements.txt

# get the version of the Python library - example
conda list pandas

# start the mlflow UI
mlflow ui --backend-store-uri sqlite:///mlflow.db

```
