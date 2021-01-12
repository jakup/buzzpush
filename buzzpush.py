#!/usr/bin/env python
import click
import requests


@click.command()
@click.option('-t', '--token', required=True, help="your application's API token")
@click.option('-u', '--user', required=True, help='the user/group key')
@click.option('--message', default='buzzpush has been invoked with the default arguments', help='Alert message')
@click.option('--url', default='https://api.pushover.net/1/messages.json')
def main(token, user, message, url):
    resp = requests.post(url, data={'token': token, 'user': user, 'message': message})
    click.echo(resp.status_code)
    click.echo(resp.text)


if __name__ == "__main__":
    main()
