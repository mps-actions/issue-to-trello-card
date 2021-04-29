import json

import click
import requests


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
@click.option('--issue')
@click.option('--key')
@click.option('--token')
def create_card_from_issue(list_id, issue, key, token):
    # credentials = {'key': key, 'token': token}
    # data = create_card(list_id, name, description, member_ids, credentials)
    # print(data.text)
    print(issue)


if __name__ == '__main__':
    create_card_from_issue()
