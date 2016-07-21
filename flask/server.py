# Sample LinkedIn Ads API integration

import os
import requests

from flask import request

# Obtain your Client ID and Client secret from LinkedIn at https://www.linkedin.com/developer/apps/
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

# LinkedIn redirect URIs must be configured in app settings
REDIRECT_URL = 'http://127.0.0.1:5000/callback'

# LinkedIn URLs
LINKEDIN_OAUTH_URL = 'https://www.linkedin.com/oauth/v2'
LINKEDIN_API_BASE_URL = 'https://api.linkedin.com/v1'

def oauth(request):
    """
    Handles LinkedIn redirect
    """
    code = request.args.get('code')
    state = request.args.get('state')
    access_token = None

    access_token = get_access_token(code, state)
    print "Access token is"
    print(access_token)

    name = get_user(access_token)[0]

    return name

def get_access_token(code, state):
    """
    Exchange code for a LinkedIn (member) access token for user
    """
    # TODO confirm state before using code
    # TODO handle user rejection
    url = LINKEDIN_OAUTH_URL + '/accessToken'

    headers = {
        'Host': 'www.linkedin.com',
        'Content-type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URL,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(url, 
        data=payload,
        headers=headers)

    if response is not None:
        results = response.json()
        if 'access_token' in results:
            token = results['access_token']
        else:
            token = None
            print '[CUSTOM] Access token not found in results'
    return token

def get_user(token):
    """
    Returns the results from people API
    """

    headers = {
        'Host': 'api.linkedin.com',
        'Connection': 'Keep-Alive',
        'Authorization': 'Bearer {token}'.format(token=token)
    }

    response = requests.get(LINKEDIN_API_BASE_URL + '/people/~?format=json', headers=headers)

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