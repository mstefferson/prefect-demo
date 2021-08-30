import prefect
from prefect import Flow, Parameter, task
from prefect.run_configs import DockerRun
from prefect.storage import Git, GitHub

# IMAGE = "prefecthq/prefect:0.15.4"
IMAGE = "prefect-dev:latest"
LOGGER = prefect.context.get("logger")


@task
def summer(x):
    # this is
    LOGGER.info("You've been informed")
    LOGGER.warning("You've been warned")
    if False:
        import numpy as np
        sums = np.sum(x)
    else:
        sums = 0
        for ii in x:
            sums += ii
    return sums

with Flow("mega-flow-git-docker") as flow:
    x = Parameter("x", default=[0, 1, 2])
    y = summer(x)

def main():
    flow.run()
    flow.run_config = DockerRun(labels=["docker"], image=IMAGE)
    flow.storage = GitHub(repo="mstefferson/prefect-demo", path="git_docker_flow.py")
    flow.register("my-demo")


if __name__ == "__main__":
    main()
