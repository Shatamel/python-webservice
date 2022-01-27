from bottle import route, run, HTTPResponse
from pymongo import MongoClient
import json
import re

client = MongoClient('mongodb://localhost:27017/')
url_regex = "^[a-z][a-z0-9+\-.]*"


def check_base(url):
    db = client.urlsdb
    urls = list(db.urls.find({}, {'_id': 0}))
    for policy in urls:
        url_name = policy.get('url')
        if url[0] == url_name:
            return policy
        else:
            continue


def parse_policy(url):
    matched_urls = check_base(url)
    if matched_urls:
        return matched_urls.get("policy")
    else:
        raise HTTPResponse(status=204)


@route('/urlinfo/1/<url:path>')
def geturls(url):
    url = re.findall(url_regex, url)
    policy = parse_policy(url)
    return json.dumps(policy)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
