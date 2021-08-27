from prefect.agent.local import LocalAgent

LocalAgent(labels=["local"]).start()
