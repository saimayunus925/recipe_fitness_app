
from pymongo import MongoClient # use this to connect to the MongoDB database
import os # use this to get CONNECTION_STRING env variable

def get_DB():
    CONNECTION_STRING = os.getenv("CONNECTION_STRING") # the connection string for our MongoDB cluster (which has the DB)
    client = MongoClient(CONNECTION_STRING) # 'client': the MongoDB client that's now connected to our MongoDB cluster
    return client['recipeDatabase'] # returns our 'recipeDatabase' DB from the cluster

def get_recipes_table():
    # returns our 'recipes' table
    recipeDatabase = get_DB() # our app database
    return recipeDatabase['recipes'] # the 'recipes' collection in our database