#!/usr/bin/env python

import argparse
import os
import requests
import yaml

# OAuth 2.0 bearer token to make API calls on behalf of LinkedIn member
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# LinkedIn API
LINKEDIN_API_BASE_URL = 'https://api.linkedin.com/v1'


def main(options):
    file =  options.file_name
    print "Reading from " + file
    f = open(file)
    dataMap = yaml.safe_load(f)
    f.close()
    results = get_user(ACCESS_TOKEN, dataMap)
    print results
    return


def get_account(dataMap):
    """ Returns results from adAccounts resource"""
    return


def get_user(token, dataMap):
    """Returns the results from people API"""
    headers = {
        'Host': 'api.linkedin.com',
        'Connection': 'Keep-Alive',
        'Authorization': 'Bearer {token}'.format(token=token)
    }

    resource = _url(dataMap['people'][0]['path'] + '?' + dataMap['people'][0]['parameters'])
    print resource
    
    if dataMap['people'][0]['verb'] == 'get':
        response = requests.get(resource,
                                headers=headers)

    if response is not None:
        results = response.json()
        user_first_name = results['firstName']
        user_last_name = results['lastName']
        user_headline = results['headline']
    else:
        results = None
        user_first_name = None
        user_last_name = None
        user_headline = None
    return user_first_name, user_last_name, user_headline


def input():
    """Gets input from external user-specified yml file"""
    p = argparse.ArgumentParser(description='Reads .yml of API endpoints METHOD RESOURCE')
    p.add_argument('-f', '--file', required=True, dest='file_name', help='file location')
    args = p.parse_args()
    return args


def _datamap(dataMap):
    """Returns help information about the format of input yaml"""
    print "dataMap is a ", type(dataMap), dataMap
    print "people items are", type(dataMap['people']), dataMap['people']
    print "ads items are", type(dataMap['accounts']), dataMap['accounts']
    print "dataMap['people'][0]['verb'] is", type(dataMap['people'][0]['verb']), dataMap['people'][0]['verb']
    return


def _url(path):
    """Builds the API URL for the resource"""
    return LINKEDIN_API_BASE_URL + path


if __name__ == '__main__':
    options = input()
    main(options)
