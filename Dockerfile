FROM manifoldai/orbyter-ml-dev:latest
RUN pip install prefect
CMD ["echo", "hello", "world"]
