start-prefect-server: ## start prefect server. you need prefect installed
	prefect backend server
	prefect server start --use-volume

start-local-agent:
	python start_local_agent.py

start-docker-agent:
	python start_docker_agent.py

dag:
	python dag.py
