
import os, requests # os: getenv() from there gets env variables
# requests: we'll use this to fetch data from the API with HTTP requests

API_KEY = os.getenv('API_KEY') # our API key

def get_content(API_URL):
    # reads in API endpoint/URL, returns content there
    return requests.get(API_URL) # we made a GET request for this URL, we're returning the HTTP response

