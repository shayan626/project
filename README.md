## ML PROJECT

import dagshub
dagshub.init(repo_owner='shayan626', repo_name='project', mlflow=True)

import mlflow
with mlflow.start_run():
mlflow.log_param('parameter name', 'value')
mlflow.log_metric('metric name', 1)
