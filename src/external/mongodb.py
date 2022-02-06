from operator import le
import os
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv('COSMOSDB_ENDPOINT')
key = os.getenv('COSMOSDB_KEY')

client = CosmosClient(endpoint, key)

DATABASE_NAME = 'ScrapLinkedInData'
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME = 'Profiles'
container = database.get_container_client(CONTAINER_NAME)

def getCurrentIndex():
    items = container.query_items(
        query='SELECT * FROM {}'.format(CONTAINER_NAME),
        enable_cross_partition_query=True)
    return len(list(items))

def insertData(data):
    container.upsert_item(data)

def getProfiles():
    items = container.query_items(
        query='SELECT * FROM {}'.format(CONTAINER_NAME),
        enable_cross_partition_query=True)
    return list(items)

print(getProfiles())

