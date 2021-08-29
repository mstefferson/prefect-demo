import prefect
from prefect import Flow
from prefect.storage import Local

from prefect import Flow, task, Parameter
from prefect.storage import GitHub
from prefect.run_configs import LocalRun
from tasks import cool_task, summer, print_a_nice_message, threshold_check, t_disp_value


import numpy as np

LOGGER = prefect.context.get("logger")
REGISTER = True

with Flow("mega-flow") as mega_flow:
    x = Parameter('x', default = [0, 1, 2])
    print_a_nice_message()
    y = summer(x)
    t_disp_value(y)
    threshold_check(y)
    cool_task()
