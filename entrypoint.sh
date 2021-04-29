#!/usr/bin/env bash

python /code/card.py \
  --list-id="${1}" \
  --google-sheet-name="${2}" \
  --token="${TRELLO_TOKEN}"