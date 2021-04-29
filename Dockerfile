FROM python:3.9.4-buster

RUN apt-get update && \
    apt-get upgrade -y

RUN pip install requests click

# COPY ./src /code
# WORKDIR /code

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

