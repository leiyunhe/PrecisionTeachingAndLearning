import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'leiyunhe'
PASSWORD = 'Craney20150421'

# The repository to add this issue to
REPO_OWNER = 'leiyunhe'
REPO_NAME = 'PrecisionTeachingAndLearning'

# issue created by creator
CREATOR = 'ruibofeng'
TIME = '2017-01-01T00:00:00Z'
payload = {'creator':CREATOR,
			'since':TIME}

def get_github_issue():
	url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
	s = requests.session()

	s.auth = (USERNAME,PASSWORD)
	r = s.get(url, params = payload)

	result = json.loads(r.text)
	issue_id = result[0]["id"]
	issue_number = result[0]["number"]

	print(issue_id,issue_number)
	return issue_id, issue_number

get_github_issue()

