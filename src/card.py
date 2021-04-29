import os
import json
import requests
import pandas as pd
import gspread
import click


def create_card(list_id, name, description='', member_ids=[], credential={}):
    url = "https://api.trello.com/1/cards"
    query = {
        'key': credential['key'],
        'token': credential['token'],
        'idList': list_id,
        'name': name,
        'desc': description,
        'idMembers': ','.join(member_ids)
    }
    return requests.post(url, params=query)


@click.command()
@click.option('--list-id')
@click.option('--google-sheet-name')
def create_card_from_issue(list_id, google_sheet_name):
    trello_credential = json.loads(os.environ.get('TRELLO_CREDENTIAL'))
    gcp_credential = json.loads(os.environ.get('GCP_CREDENTIAL'))
    with open(os.environ.get('GITHUB_EVENT_PATH')) as f:
        issue = json.load(f)['issue']
    data = create_card(list_id, issue['title'], issue['body'], credential=trello_credential)
    print(data.text)
    print(json.dumps(issue, indent=True))


if __name__ == '__main__':
    create_card_from_issue()
