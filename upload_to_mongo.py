import csv
import os
from pymongo import MongoClient
from configs1 import mongo_host, mongo_port, db_name, collection_name


def is_valid_value(keys,value):
    """ Check if the value is valid (not None, NaN, or empty string). """
    if (value is None or value == '' or (isinstance(value, str) and value.lower() in ['nan', 'none','0'])) or keys.startswith('Unnamed'):
        return False
    return True

# Function to read and import CSV data into MongoDB
def import_csv(csv_file_path, file_name, collection):
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        csv_data = []

        for row in reader:
            # Clean the row data
            cleaned_row = {key: str(value).rstrip('.0') if isinstance(value, float) and value.is_integer() else str(value)
                           for key, value in row.items() if is_valid_value(key,value)}

            if cleaned_row:  # Only append if row is not empty after cleaning
                csv_data.append(cleaned_row)

        if csv_data:
            collection.insert_many(csv_data)
            print(f"Inserted {len(csv_data)} documents into MongoDB collection '{collection.name}' from file {file_name}")
        else:
            print(f"No data found in file {csv_file_path}")

def uploadToMongo(csv_directory,mongo_host=mongo_host, mongo_port=mongo_port, db_name=db_name, collection_name=collection_name):
    # Iterate over CSV files in the directory and import each one
    client = MongoClient(host=mongo_host, port=mongo_port)
    # Uncomment the following line if authentication is enabled
    # client = MongoClient(host=mongo_host, port=mongo_port, username=mongo_user, password=mongo_pass)

    # Specify the database and collection
    db = client[db_name]
    collection = db[collection_name]
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_directory, filename)
            import_csv(file_path, filename,collection)

    # Close the MongoDB connection
    client.close()

    print(f"CSV import completed from {csv_directory}.")
    print('-'*40)
