import numpy as np
import prefect
from prefect import Flow, Parameter, task
from prefect.run_configs import LocalRun
from prefect.storage import GitHub, Local

from tasks import cool_task

LOGGER = prefect.context.get("logger")
REGISTER = True


def disp_value(y, logger=None):
    if logger is None:
        import logging

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(relativeCreated)6d %(threadName)s %(message)s",
        )
        logger = logging.getLogger(__name__)
    logger.info(f"Input is {y}")


@task
def t_disp_value(y):
    disp_value(y, LOGGER)


@task(log_stdout=True)
def print_a_nice_message():
    print("A secret message!")
    nice_messages = [
        "You got this!",
        "Keep up the hard work!",
        "Wow, you're doing such a great job",
    ]
    print(np.random.choice(nice_messages))


@task
def threshold_check(y):
    threshold = 5
    if y > threshold:
        raise ValueError(f"y = {y} > {threshold}. That's bad")
    LOGGER.info(f"y = {y} <= {threshold}. I like that!")


@task
def task(x):
    # this is not captured
    print("I'm in the task")
    # this is
    LOGGER.info("You've been informed")
    LOGGER.warning("You've been warned")
    return np.sum(x)


with Flow("local-example") as flow:
    x = Parameter("x", default=[0, 1, 2])
    print_a_nice_message()
    y = task(x)
    t_disp_value(y)
    threshold_check(y)
    cool_task()

flow.run()
flow.run_config = LocalRun(labels=["local"])
flow.storage = Local()
if REGISTER:
    print("Registering")
    flow.register("my-demo")
