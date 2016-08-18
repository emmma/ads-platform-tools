# Purpose
Sample tools and utilities for LinkedIn Ads APIs

### Installation
To contribute to the project or use sample scripts, run the following commands in your terminal:


```bash
# clone the repository

git clone git@github.com:emmma/ads-platform-tools.git
cd python

# install dependencies
pip install -r requirements.txt
```

Set up `ACCESS_TOKEN` for your local machine.  Replace the `<value>` with the OAuth 2.0 Bearer token for the user (LinkedIn member) on whose behalf you'd like to make API calls

```bash
export ACCESS_TOKEN='<value>'
```

### Usage
To run the python script, type the following command in terminal:

```bash
python smoke.py -f input.yml
```
Sample input.yml is provided for demo purposes.
