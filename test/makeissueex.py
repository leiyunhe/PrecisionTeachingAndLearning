import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'leiyunhe'
PASSWORD = 'Craney20150421'

# The repository to add this issue to
REPO_OWNER = 'leiyunhe'
REPO_NAME = 'PrecisionTeachingAndLearning'

def make_github_issue(title, body=None, milestone=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    # session = requests.session(auth=(USERNAME, PASSWORD))
    s = requests.session()
    s.auth = (USERNAME,PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             #'assignee': assignee,
             'milestone': milestone,
             'labels': labels}
    # Add the issue to our repository
    # with open('issue.json','w') as f:
    #     d = json.dump(issue, f)

    # r = s.post(url, d)
    # print(r)
    r = s.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', r.content) 

make_github_issue('creatissue', 'Body text', None, ['bug'])