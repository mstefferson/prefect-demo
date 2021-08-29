import prefect
from prefect import task
from funcs import disp_value
import numpy as np

LOGGER = prefect.context.get("logger")

@task
def cool_task():
    LOGGER.info("I'm a cool task")

@task
def t_disp_value(y):
    disp_value(y, LOGGER)

@task(log_stdout=True)
def print_a_nice_message():
    print("A secret message!")
    nice_messages = [
        "You got this!",
        "Keep up the hard work!",
        "Wow, you're doing such a great job"
    ]
    print(np.random.choice(nice_messages))


@task
def threshold_check(y):
    threshold = 5
    if y > threshold:
        raise ValueError(f"y = {y} > {threshold}. That's bad")
    LOGGER.info(f"y = {y} <= {threshold}. I like that!")

@task
def summer(x):
    # this is not captured
    print("I'm in the task")
    # this is
    LOGGER.info("You've been informed")
    LOGGER.warning("You've been warned")
    return np.sum(x)
