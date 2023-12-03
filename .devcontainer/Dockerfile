FROM python:latest

# these are staples!
# you do not have to include in the requirements.txt
RUN python3 -m pip install -U black pylint pytest ipykernel

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

RUN useradd -ms /bin/bash vscode

USER vscode
WORKDIR /home/vscode
