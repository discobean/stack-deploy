FROM python:2.7-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY stack-deploy /usr/bin/stack-deploy
WORKDIR /stacks
CMD /bin/bash

