FROM python:3.7.9-slim-buster
LABEL Maintainer="adesabastine5@gmail.com"
WORKDIR /usr/app/src
COPY requirements.txt ./
COPY pull-requests.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./pull-requests.py"]