import numpy as np
from prefect import Flow, Parameter, task
from prefect.run_configs import LocalRun
from prefect.storage import Git, GitHub

from tasks import cool_task, print_a_nice_message, summer, t_disp_value, threshold_check

with Flow("mega-flow-git") as flow:
    x = Parameter("x", default=[0, 1, 2])
    print_a_nice_message()
    y = summer(x)
    t_disp_value(y)
    threshold_check(y)
    cool_task()

flow.run()
flow.run_config = LocalRun(labels=["local"])
flow.storage = GitHub(repo="mstefferson/prefect-demo", path="git_flow.py")
flow.register("my-demo")
