# Purpose
Sample Flask app that integrates with LinkedIn APIs

## Current Functionality
* Begins OAuth 2.0 dance with user
* Generates an access token for the user (LinkedIn member)
* Calls the /people/~ endpoint to determine the first name of user

# Demo
This sample app has been configured to run on localhost.
```

### Installation
If you'd like to contribute to the project or try an unreleased version of the sample Flask app locally, run the following commands in your terminal:


```bash
# clone the repository

git clone git@github.com:emmma/ads-platform-tools.git
cd flask

# install dependencies
pip install -r requirements.txt

#set up required environment variables for Flask.
export FLASK_APP=app.py

# (optional) enable debugging for the app
export FLASK_DEBUG=1
```

Set up `CLIENT_ID` and `CLIENT_SECRET` for your local machine.  Replace the `<value>` with the exact value that is found in the **OAuth Settings** for your app.

```bash
export CLIENT_ID='<value>'
export CLIENT_SECRET='<value>' 
```
### Usage
To run the app, type the following command in your terminal:
```bash
flask run
```
This will launch the app on your machine.  Flask will also log debugging information in the terminal.  You should see a response similar to the following below:
>> Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

You can go to a web browser of your choice and type in the URL provided (e.g. http://127.0.0.1:5000/) to interact with the app.

## Additional Resources

#### Flask

* [Flask](http://flask.pocoo.org/)
* [Application Errors](http://flask.pocoo.org/docs/0.11/errorhandling/)

#### Extraneous

* [HTTP Status and Error Codes](https://cloud.google.com/storage/docs/json_api/v1/status-codes)
* [Python `requests.status codes`](https://github.com/kennethreitz/requests/blob/master/requests/status_codes.py)
* [Deploying Python and Django apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)

## TODO
* Optimize error handling for retry() for HTTP 4XX and HTTP 5XX errors
* Set up better logging for errors and exceptions
* Set up automated tests: capture exceptions and edge cases
* Make additional calls third-party APIs