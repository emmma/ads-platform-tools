#!/usr/bin/env python

import os
import requests

# OAuth 2.0 bearer token to make API calls on behalf of LinkedIn member
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# LinkedIn API
LINKEDIN_API_BASE_URL = 'https://api.linkedin.com/v1'


def main():
    results = get_user(ACCESS_TOKEN)
    print results
    return


def get_user(token):
    """
    Returns the results from people API
    """
    headers = {
        'Host': 'api.linkedin.com',
        'Connection': 'Keep-Alive',
        'Authorization': 'Bearer {token}'.format(token=token)
    }

    response = requests.get(LINKEDIN_API_BASE_URL + '/people/~?format=json',
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

if __name__ == '__main__':
    main()
