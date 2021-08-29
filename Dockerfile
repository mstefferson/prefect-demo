FROM manifoldai/orbyter-ml-dev:latest
RUN pip install prefect[github] \
    pip install prefect[aws] 
WORKDIR /
CMD ["echo", "hello", "world"]
