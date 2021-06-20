#!/usr/bin/python3

import json
import os

import click
import requests


@click.group()
def anity():
    pass


@anity.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--dev', is_flag=True, help='run against the staging api')
def update(path, dev):
    api_key = _get_api_key(dev)
    if api_key is None:
        return
    url = _url('v1/suite', dev)

    name = os.path.basename(path)
    with open(path, 'rb') as f:
        resp = requests.put(
            url,
            files={
                'package': (name, f.read()),
                'api_key': (None, api_key),
            }
        )
        if resp.status_code != 200:
            print(f'failed to update tests [{resp.status_code}]')


@anity.command()
@click.option('--dev', is_flag=True, help='run against the staging api')
def invoke(dev):
    api_key = _get_api_key(dev)
    if api_key is None:
        return
    url = _url('v1/invoke', dev)
    resp = requests.post(url, json={'api_key': api_key})
    if resp.status_code != 200:
        print(f'failed to invoke api [{resp.status_code}]')
    results = resp.json()
    ok = True
    for t in results:
        print(t)
        if t['status'] != 'pass':
            ok = False
        print(f"{t['service_name']} {t['test_name']} {t['timestamp']} {t['runtime']} {t['status']}")

    if not ok:
        raise ValueError('tests failed')


def _get_api_key(dev):
    env = 'ANITY_DEV_API_KEY' if dev else 'ANITY_API_KEY'
    api_key = os.environ.get(env, None)
    if api_key is None:
        print(f"missing '{env}' environment variable")
    return api_key


def _url(path, dev):
    domain = 'api.dev.anity.io' if dev else 'api.anity.io'
    return f'https://{domain}/{path}'


if __name__ == '__main__':
    anity()
