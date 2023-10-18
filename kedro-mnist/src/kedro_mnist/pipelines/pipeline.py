from kedro.pipeline import node, Pipeline
from kedro_mnist.pipelines.nodes import load_data
from kedro_mnist.pipelines.nodes import create_and_train_model
from kedro_mnist.pipelines.nodes import evaluate_model

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(load_data, outputs=["X_train", "X_test", "y_train", "y_test"]),
            node(create_and_train_model, inputs=["X_train", "y_train"], outputs="model"),
            node(evaluate_model, inputs=["model", "X_test", "y_test"], outputs="value"),
        ]
    )