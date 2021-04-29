#!/usr/bin/env bash

python /code/card.py \
  --list-id="${1}" \
  --name="${2}" \
  --description="${3}" \
  --key="${TRELLO_KEY}" \
  --token="${TRELLO_TOKEN}"