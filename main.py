
import os, requests # os: getenv() from there gets env variables
# requests: we'll use this to fetch data from the API with HTTP requests

API_KEY = os.getenv('API_KEY') # our API key

def get_content(URL):
    # reads in API endpoint/URL, returns content there
    return requests.get(URL) # we made a GET request for this URL, we're returning the HTTP response

API_URL_NUTRIENTS = os.getenv('API_URL_NUTRIENTS') # the API URL for getting recipes by nutrients
API_URL_INGREDIENTS = os.getenv('API_URL_INGREDIENTS') # the API URL for getting recipes by ingredients



