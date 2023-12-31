
import os, requests, sqlite3 # os: getenv() from there gets env variables
# requests: we'll use this to fetch data from the API with HTTP requests
# sqlite3: we'll use this to make and connect to a SQL database for storing/querying the API data

API_KEY = os.getenv('API_KEY') # our API key

def get_response(URL):
    # reads in API endpoint/URL, sends a GET request there, returns response status code and response data
    return (requests.get(URL).status_code, requests.get(URL).content)

API_URL_NUTRIENTS = os.getenv('API_URL_NUTRIENTS') # the API URL for getting recipes by nutrients
API_URL_INGREDIENTS = os.getenv('API_URL_INGREDIENTS') # the API URL for getting recipes by ingredients

