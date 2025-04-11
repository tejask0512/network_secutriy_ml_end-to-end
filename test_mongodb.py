from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
# Properly encode username and password
uri=os.getenv('MONGO_DB_URL')
# Construct the URI safely

# Create a new client and connect
client = MongoClient(uri, server_api=ServerApi('1'))

# Test connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
