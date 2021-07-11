import base64
import os
import sys

import click
import requests


@click.group()
def cli():
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--dev', is_flag=True, help='run against the staging api')
def update(path, dev):
    api_key = _get_api_key(dev)
    if api_key is None:
        return
    url = _url(f'scheduler/v1/suite/{api_key}', dev)

    with open(path, 'rb') as f:
        resp = requests.put(url, data=base64.b64encode(f.read()))
        if resp.status_code != 200:
            print(f'failed to update tests [{resp.status_code}]')


@cli.command()
@click.option('--dev', is_flag=True, help='run against the staging api')
def invoke(dev):
    api_key = _get_api_key(dev)
    if api_key is None:
        return
    url = _url(f'scheduler/v1/invoke/{api_key}', dev)
    resp = requests.post(url)
    if resp.status_code != 200:
        print(f'failed to invoke api [{resp.status_code}]')
    results = resp.json()
    ok = True
    for t in results:
        if t['status'] != 'pass':
            ok = False
        print(f"{t['service_name']} {t['test_name']} {t['timestamp']} {t['runtime']} {t['status']}")

    if not ok:
        sys.exit(-1)


@cli.command()
@click.option('--dev', is_flag=True, help='run against the staging api')
def invoke_async(dev):
    api_key = _get_api_key(dev)
    if api_key is None:
        return
    url = _url(f'scheduler/v1/invoke/{api_key}/async', dev)
    resp = requests.post(url)
    if resp.status_code != 200:
        print(f'failed to invoke api [{resp.status_code}]')


def _get_api_key(dev):
    env = 'ANITY_DEV_API_KEY' if dev else 'ANITY_API_KEY'
    api_key = os.environ.get(env, None)
    if api_key is None:
        print(f"missing '{env}' environment variable")
    return api_key


def _url(path, dev):
    domain = 'api2.dev.anity.io' if dev else 'api2.anity.io'
    return f'https://{domain}/{path}'
