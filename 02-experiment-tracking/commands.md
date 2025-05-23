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

# install click to use the 'preprocess_data.py' file provided
conda install anaconda::click

# apply the preprocessing step using the 'preprocess_data.py'
python preprocess_data.py --raw_data_path data/ --dest_path ./output

```

### Configuration of the MLflow on the code - example

```bash
# configuration of the mlflow in the beginning of the code
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("homework-experiment_tracking")

# ...
# the body code
# ...

with mlflow.start_run():
    mlflow.set_tag("developer", "luciana")
    mlflow.log_param("alpha", alpha)

    # create an instance of the model
    # fit
    # calculate the predictions
    # calculate the evaluation metric

    mlflow.log_metric("rmse", rmse)

```

### Using the MLflow autolog

```bash
# autolog configuration
  mlflow.autolog()

    with mlflow.start_run():
        # create an instance of the model
        # fit
        # calculate the predictions
        # calculate the evaluation metric
```
