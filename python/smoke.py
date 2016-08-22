#!/usr/bin/env python

import argparse
import json
import os
import pprintpp
import requests
import requests.packages.urllib3
import yaml

import simplejson
from time import sleep

requests.packages.urllib3.disable_warnings()

# OAuth 2.0 bearer token to make API calls on behalf of LinkedIn member
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# LinkedIn API
LINKEDIN_API_BASE_URL = 'https://api.linkedin.com/v2'


def main(options):
    file_name = options.file_name
    dataMap = parse_input(file_name)
    dataMap = build_requests(dataMap)
    results = make_requests(dataMap)
    output(results)
    return


def build_requests(dataMap):
    """Creates the API requests from input"""

    for restli_resource in dataMap:
        for resource_method in dataMap[restli_resource]:
            url = _url(resource_method['path'], resource_method['parameters'])
            resource_method['url'] = url
    return dataMap


def make_requests(dataMap):
    headers = {
        'Host': 'api.linkedin.com',
        'Connection': 'Keep-Alive',
        'Authorization': 'Bearer {token}'.format(token=ACCESS_TOKEN)
    }

    for restli_resource in dataMap:
        for resource_method in dataMap[restli_resource]:
            response = None
            if resource_method['verb'] == 'BATCH_GET' or 'GET' or 'FINDER':
                try:
                    response = requests.get(resource_method['url'],
                                            headers=headers)
                except requests.exceptions.ConnectionError, e:
                    print e
                    sleep(5)
            elif resource_method['verb'] == 'POST':
                pass
            elif resource_method['verb'] == 'PUT':
                pass
            if response is not None and response.status_code is not 400:
                resource_method['api_results'] = response.json()
            else:
                resource_method['api_results'] = response
                print "error response"
    return dataMap


def get_input():
    """Gets input from external user-specified yml file"""
    p = argparse.ArgumentParser(description='Makes API calls')
    p.add_argument('-f', '--file', required=True,
                   dest='file_name', help='file location')
    args = p.parse_args()
    return args


def parse_input(file_name):
    """Parses user-defined yaml file"""
    with open(file_name, "r") as f:
        dataMap = yaml.safe_load(f)
    return dataMap


def output(dataMap):
    with open("output.txt", "w") as f:
        for restli_resource in dataMap:
            for resource_method in dataMap[restli_resource]:
                f.write(resource_method['verb'])
                f.write(" ")
                f.write(resource_method['url'])
                f.write("\n")
                f.write("----------------------------------------------")
                f.write("\n")
                output = resource_method['api_results']
                try:
                    f.write(json.dumps(output, indent=4, sort_keys=True))
                except KeyError, e:
                    print e
                f.write("\n")
                f.write("\n")
    return


def _url(path, parameters):
    """Builds the API URL for the resource"""
    if parameters is not None:
        url = LINKEDIN_API_BASE_URL + path + str(parameters)
    else:
        url = LINKEDIN_API_BASE_URL + path
    return url


if __name__ == '__main__':
    options = get_input()
    main(options)
