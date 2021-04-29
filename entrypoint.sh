#!/usr/bin/env bash

python /code/card.py \
  --list-id="${1}" \
  --issue="${2}" \
  --key="${TRELLO_KEY}" \
  --token="${TRELLO_TOKEN}"