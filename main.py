from bottle import route, run
from policy import Policy
import json
import re

url_regex = "^[a-z][a-z0-9+\-.]*"

@route('/urlinfo/1/<url:path>')
def geturls(url):
    url = re.findall(url_regex, url)
    policy = Policy(url)
    return json.dumps(policy.parse_policy())


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
