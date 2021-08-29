import numpy as np
import prefect
from prefect import Flow, Parameter, task
from prefect.run_configs import LocalRun
from prefect.storage import GitHub, Local

from tasks import cool_task, print_a_nice_message, summer, t_disp_value, threshold_check

LOGGER = prefect.context.get("logger")
REGISTER = True

with Flow("mega-flow") as mega_flow:
    x = Parameter("x", default=[0, 1, 2])
    print_a_nice_message()
    y = summer(x)
    t_disp_value(y)
    threshold_check(y)
    cool_task()
