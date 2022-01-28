from pymongo import MongoClient

urls = [{'id': 1, 'url': 'google.com', 'policy': 'blocked'},
        {'id': 2, 'url': 'facebook.com', 'policy': 'blocked'},
        {'id': 3, 'url': 'cisco.com', 'policy': 'unblocked'},
        {'id': 4, 'url': 'netflix.com', 'policy': 'unblocked'}]

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.urlsdb

    db.urls.insert_many(urls)