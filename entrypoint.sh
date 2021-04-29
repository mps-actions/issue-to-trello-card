#!/usr/bin/env bash

python /code/card.py \
  --list-id="${1}" \
  --key="${TRELLO_KEY}" \
  --token="${TRELLO_TOKEN}"