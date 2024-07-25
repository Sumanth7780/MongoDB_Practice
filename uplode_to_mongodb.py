import json
from pymongo import MongoClient

def load_json_to_mongodb(file_path, db_name, collection_name):
    # Step 1: Load the JSON file
    with open(file_path) as file:
        data = json.load(file)

    # Step 2: Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]

    # Step 3: Insert the data
    # If the data is a list of documents, use insert_many. Otherwise, use insert_one.
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

    print(f"Data from {file_path} has been inserted successfully into the {collection_name} collection!")

# File paths and MongoDB details
files_to_upload = [
    {"file_path": "data/cart_history.json", "db_name": "vegetable_data", "collection_name": "cart_history"},
    {"file_path": "data/VegetablePrices.json", "db_name": "vegetable_data", "collection_name": "vegetable_prices"}
]

# Upload each file
for file_info in files_to_upload:
    load_json_to_mongodb(file_info['file_path'], file_info['db_name'], file_info['collection_name'])
