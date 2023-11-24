FROM python:3.9-slim
WORKDIR /home/app
RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir ariadne
RUN pip install --no-cache-dir requests
