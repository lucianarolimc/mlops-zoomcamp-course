import os
import pickle
import click

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

import mlflow

# mlflow configuration
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("homework-experiment_tracking")


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    # mlflow.autolog()

    with mlflow.start_run():

        mlflow.set_tag("developer", "lucianac")

        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        # saving the model
        # models_dir = './models/'
        models_local_path = './models/random_forest_model.bin'
        with open(models_local_path, 'wb') as f_out:
            pickle.dump(rf, f_out)

        rmse = root_mean_squared_error(y_val, y_pred)
        mlflow.log_metric("rmse", rmse)

        mlflow.log_artifact(local_path=models_local_path, artifact_path="artifacts")
    
    


if __name__ == '__main__':
    run_train()
