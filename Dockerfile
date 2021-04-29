FROM python:3.9.4-buster

RUN apt-get update && \
    apt-get upgrade -y

RUN pip install requests click google-api-python-client \
    google-auth-httplib2 google-auth-oauthlib gspread \
    numpy pandas

COPY ./src /code
WORKDIR /code

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

