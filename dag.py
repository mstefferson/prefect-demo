from prefect import Flow
from prefect.storage import Git

from prefect import Flow, task
from prefect.storage import GitHub

import numpy as np

@task
def task_2(x):
    return np.sum(x)

with Flow("git-example") as flow:
    y = task_2([1, 2, 3])
    print("Flow done!")

flow.run()

flow.storage = GitHub(repo="mstefferson/prefect-demo", path="dag.py")
flow.register("tutorial")
