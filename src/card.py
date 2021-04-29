import os
from datetime import datetime
import json
import requests
import pandas as pd
import gspread
import click


@click.command()
@click.option('--list-id')
@click.option('--google-sheet-name')
def create_card_from_issue(list_id, google_sheet_name):
    with open(os.environ.get('GITHUB_EVENT_PATH')) as f:
        issue = json.load(f)['issue']

    # Create the card on Trello for the issue.
    trello_credential = json.loads(os.environ.get('TRELLO_CREDENTIAL'))
    url = "https://api.trello.com/1/cards"
    trello_query = {
        'key': trello_credential['key'],
        'token': trello_credential['token'],
        'idList': list_id,
        'name': issue['title'],
        'desc': issue['html_url'],
    }
    res = requests.post(url, params=trello_query)
    if res.status_code != 200:
        raise Exception(f'Failed to create the card for issue #{issue["number"]}.')
    card = res.json()

    # Create log on Google Sheet
    columns = ['issue id', 'issue number', 'created by (id)', 'created by (username)',
               'issue url', 'list id', 'card id', 'card url', 'located at', 'name']
    gcp_credential = json.loads(os.environ.get('GCP_CREDENTIAL'))
    google_sheet = gspread.service_account_from_dict(gcp_credential)
    spreadsheet = google_sheet.open(google_sheet_name)
    try:
        worksheet = spreadsheet.worksheet('issue-tracker')
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet('issue-tracker', rows=1000, cols=len(columns))
    df = pd.DataFrame(worksheet.get_all_records(), columns=columns)
    row_values = [issue['id'], issue['number'], issue['user']['id'], issue['user']['login'],
                  issue['html_url'], card['idList'], card['id'], card['shortUrl'],
                  datetime.utcnow().strftime('%Y-%m-%dT%H%M%S:%fZ'), card['name']]
    df = df.append({key: value for key, value in zip(columns, row_values)})
    print(df)
    worksheet.update([df.columns.values.tolist(), ] + df.values.tolist())


if __name__ == '__main__':
    create_card_from_issue()
