DEV_IMAGE=prefect-dev
DEV_TAG=latest
DEV_FULL=$(DEV_IMAGE):$(DEV_TAG)

build-docker:
	docker build . -t $(DEV_FULL)

bash: build-docker ## Provides an interactive bash shell in the container
	docker run -it -v $(PWD):/mnt $(DEV_FULL) bash

start-prefect-server: ## start prefect server. you need prefect installed
	prefect backend server
	prefect server start --use-volume

start-local-agent:
	python start_local_agent.py

start-docker-agent:
	python start_docker_agent.py

dag:
	python dag.py
