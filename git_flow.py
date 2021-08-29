from prefect import Flow
from prefect.storage import Git

from prefect import Flow, task
from prefect.storage import GitHub
from prefect.run_configs import LocalRun
from prefect import Flow, task, Parameter

import numpy as np
from tasks import cool_task, summer, print_a_nice_message, threshold_check, t_disp_value

with Flow("mega-flow-git") as flow:
    x = Parameter('x', default = [0, 1, 2])
    print_a_nice_message()
    y = summer(x)
    t_disp_value(y)
    threshold_check(y)
    cool_task()

flow.run()
flow.run_config = LocalRun(labels=["local"])
flow.storage = GitHub(repo="mstefferson/prefect-demo", path="git_flow.py")
flow.register("my-demo")
