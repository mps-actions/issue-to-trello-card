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
@click.option('--name')
@click.option('--description', default='')
@click.option('--member-ids', default=[])
@click.option('--key')
@click.option('--token')
def create_card_command(list_id, name, description, member_ids, key, token):
    credentials = {'key': key, 'token': token}
    data = create_card(list_id, name, description, member_ids, credentials)
    print(data.json())


if __name__ == '__main__':
    create_card_command()
