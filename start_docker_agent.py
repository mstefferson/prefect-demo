import os

from prefect.agent.docker import DockerAgent

volumes = []
#volumes = [f"{os.getcwd()}:/mnt"]

DockerAgent(
    labels=["docker"], volumes=volumes, show_flow_logs=True
).start()
