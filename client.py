# Sample LinkedIn Ads API integration

import os
import requests
import webbrowser

# Obtain your Client ID and Client secret from LinkedIn at https://www.linkedin.com/developer/apps/
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

# LinkedIn redirect URIs must be configured in app settings
REDIRECT_URL = 'http://127.0.0.1:5000/oauth'

# LinkedIn URLs
LINKEDIN_OAUTH_URL = 'https://www.linkedin.com/oauth/v2'

def prompt():
    get_authorization_code()
    return

def get_authorization_code():
    """
    Redirects user to LinkedIn to confirm authorization
    """
    url = LINKEDIN_OAUTH_URL + '/authorization'
    payload = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URL,
        'state': 'EmmaIsAwesome',
        'scope': 'rw_company_admin rw_ad_campaigns r_basicprofile r_emailaddress'
    }

    response = requests.get(url, params=payload)
    redirect_url = response.url
    webbrowser.open(redirect_url, new=0, autoraise=True)
    return

if __name__ == '__main__':
    main()