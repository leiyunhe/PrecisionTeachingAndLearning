
import json
import requests

USERNAME = 'leiyunhe'
PASSWORD = 'Craney20150421'

REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'

LABEL = 'task'
STATE = 'all'

TIME = '2017-01-01T00:00:00Z'

payload1 = {'state':STATE,
			'since':TIME} 
def list_task_issue_number():

	url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
	#url = 'https://api.github.com/orgs/%s/issues' % (ORG_NAME)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url,params = payload1)
	result = json.loads(r.text)
#	print(result)
	ls = []
	for x in result:
		m = [x["url"],x["number"]]
		ls.append(m)
	return ls

# r = list_task_issue_number()
# print(len(r))

# ISSUE_NUMBER = '264'
payload2 = {'labels': LABEL,
			'state': STATE}
def submit_task_issue(ISSUE_NUMBER):
	'''
	List comments on an issue
	return: user_name, comments_url, created_at_time
	DOC  https://developer.github.com/v3/issues/comments/
	'''
	url = 'https://api.github.com/repos/%s/%s/issues/%s/comments' % (REPO_OWNER, REPO_NAME,ISSUE_NUMBER)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url,params = payload2)
	result = json.loads(r.text)
	ls = []
	for x in result:
		# m = [x["url"],x["created_at"],x["user"]]
		# m = [x["url"],x["created_at"],x["user"]["login"]]
		m = [x["created_at"],x["user"]["login"]]		
		ls.append(m)
	return ls

# r = submit_task_issue()
# print(r)


# issue_number_list = list_task_issue_number()
# for s in issue_number_list:
# 	v = submit_task_issue(s[1])

# 	for user_info in v:
# 		print(user_info)

payload3 = {'state':STATE,
			'since':TIME} 
def get_issue_comments_by_chap():

	url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url,params = payload3)
	result = json.loads(r.text)
#	print(result)
	ls = []
	for x in result:
		# m = [x["url"],x["number"]]
		m = x["title"]
		if m in CHAP_NUMBER：
			dic["user"]["login"]
		ls.append(m)
	return ls


	如果title中包含有chap7,那么就把这个值赋给chap7_time
