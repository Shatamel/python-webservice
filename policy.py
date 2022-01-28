from bottle import HTTPResponse
from pymongo import MongoClient


class Policy:
    client = MongoClient('mongodb://localhost:27017/')

    def __init__(self, url):
        self.url = url

    def check_base(self):
        db = self.client.urlsdb
        urls = list(db.urls.find({}, {'_id': 0}))
        for policy in urls:
            url_name = policy.get('url')
            if self.url[0] == url_name:
                return policy

    def parse_policy(self):
        matched_urls = self.check_base()
        if matched_urls:
            return matched_urls.get("policy")
        else:
            raise HTTPResponse(status=204)
