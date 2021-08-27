from prefect import Flow
from prefect.storage import Git

from prefect import Flow, task
from prefect.storage import GitHub
from prefect.run_configs import LocalRun

import numpy as np

@task
def task(x):
    print("I'm in the task")
    return np.sum(x)

with Flow("git-example") as flow:
    y = task([1, 2, 3])
    print("Flow done!")

flow.run()
flow.run_config = LocalRun(labels=["local"])
flow.storage = GitHub(repo="mstefferson/prefect-demo", path="dag.py")
flow.register("tutorial")
