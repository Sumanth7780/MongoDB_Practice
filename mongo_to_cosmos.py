from pymongo import MongoClient,errors

# MongoDB connection string
mongo_client = MongoClient("mongodb://localhost:27017")

# Database and collection names
db_name = "vegetable_data"
collections = ["cart_history", "vegetable_prices"]

# Fetch data from MongoDB
db = mongo_client[db_name]
data = {}
for collection in collections:
    data[collection] = list(db[collection].find())

print("Data fetched from MongoDB")
import urllib.parse
# CosmosDB connection string (using MongoDB API)
# CosmosDB credentials
username = 'sumanthsampledatabase'
password = 'Temp@1234'

# URL-encode the username and password
encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)
cosmos_connection_string = f'mongodb+srv://{encoded_username}:{encoded_password}@sampledatabase123.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000'
print(cosmos_connection_string)
# Initialize CosmosDB client
try:
    cosmos_client = MongoClient(cosmos_connection_string)
    cosmos_db = cosmos_client[db_name]

    # Insert data into CosmosDB
    for collection in collections:
        cosmos_collection = cosmos_db[collection]
        if data[collection]:
            cosmos_collection.insert_many(data[collection])

    print("Data imported to CosmosDB")
except errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
except errors.OperationFailure as e:
    print(f"Authentication failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
