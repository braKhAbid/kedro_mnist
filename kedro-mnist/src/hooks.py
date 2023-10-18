def register_pipelines():
    from kedro_mnist.pipelines.pipeline import create_pipeline
    return {
        "pipeline": create_pipeline
    }