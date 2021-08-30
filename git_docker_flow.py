import prefect
from prefect import Flow, Parameter, task
from prefect.run_configs import DockerRun
from prefect.storage import Git, GitHub
from mega_flow import flow

IMAGE = "prefecthq/prefect:0.15.4"
# IMAGE = "prefect-dev:latest"
LOGGER = prefect.context.get("logger")


def main():
    flow.run()
    flow.run_config = DockerRun(labels=["docker"], image=IMAGE)
    flow.storage = GitHub(repo="mstefferson/prefect-demo", path="mega_flow.py")
    flow.register("my-demo")


if __name__ == "__main__":
    main()
