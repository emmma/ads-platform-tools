#!/usr/bin/env python

import argparse
import json
import os
import pprintpp
import requests
import requests.packages.urllib3
import yaml

from time import sleep

requests.packages.urllib3.disable_warnings()

# OAuth 2.0 bearer token to make API calls on behalf of LinkedIn member
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# LinkedIn API
LINKEDIN_API_BASE_URL = 'https://api.linkedin.com/v2'


def main(options):
    file = options.file_name
    f = open(file)
    dataMap = yaml.safe_load(f)
    f.close()
    get_resource(dataMap)
#    with open("output.json", "w") as f:
#        f.write(results)
    return


def get_resource(dataMap):
    """ Returns results from resources in input yaml file"""

    for resource in dataMap:
        for item in dataMap[resource]:
            verb = item['verb']
            path = item['path']
            parameters = item['parameters']
            _line()
            url = _url(path, parameters)
            results = make_request(url, verb)
    return results


def make_request(url, verb):
    headers = {
        'Host': 'api.linkedin.com',
        'Connection': 'Keep-Alive',
        'Authorization': 'Bearer {token}'.format(token=ACCESS_TOKEN)
    }

    if verb == 'get' or 'finder':
        try:
            response = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            sleep(5)
    else:
        response = None

    if response is not None and response.status_code is not 400:
        pprintpp.pprint(response.json())
    return


def input():
    """Gets input from external user-specified yml file"""
    p = argparse.ArgumentParser(description='Makes API calls')
    p.add_argument('-f', '--file', required=True,
                   dest='file_name', help='file location')
    args = p.parse_args()
    return args


def _url(path, parameters):
    """Builds the API URL for the resource"""
    if parameters is not None:
        url = LINKEDIN_API_BASE_URL + path + str(parameters)
    else:
        url = LINKEDIN_API_BASE_URL + path
    print url
    _line()
    return url


def _line():
    print "--------------------------------------------------"
    return


if __name__ == '__main__':
    options = input()
    main(options)
