from bottle import route, run, HTTPResponse
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')


def parse_policy(base, url):
    matched_urls = []
    for policy in base:
        url_name = policy.get('url')
        if url[0] == url_name:
            matched_urls = policy
            break
        else:
            continue
    if matched_urls:
        return matched_urls.get("policy")
    else:
        raise HTTPResponse(status=204)


@route('/urlinfo/<url:path>')
def geturls(url):
    db = client.urlsdb
    urls = list(db.urls.find({}, {'_id': 0}))
    url = url.split("/")
    policy = parse_policy(urls, url)

    return json.dumps(policy)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
