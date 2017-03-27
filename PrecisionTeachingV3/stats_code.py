import requests
import json
def statics(USERNAME):
    # GET /repos/:owner/:repo/stats/contributors
    url = 'https://api.github.com/repos/%s/Py103/stats/contributors' % (USERNAME)
    s = requests.session()
    print(s)
    s.auth = (USERNAME,PASSWORD)
    r = s.get(url)
    result = json.loads(r.text)
    # print(result)
    addition = deletion = commits = 0
    for item in result:
    #     print(item['weeks'])
        if item['author']['login'] == USERNAME:
            print(item['author']['login'],item["weeks"])
            for m in item["weeks"]:
                addition += m['a']
                deletion += m['d']
                commits += m['c']

    return (addition,deletion,commits)