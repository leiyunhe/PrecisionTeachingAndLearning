
import json
import requests

USERNAME = 'leiyunhe'
PASSWORD = 'Craney20150421'

REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'

LABEL = 'task'
STATE = 'all'

TIME = '2017-01-01T00:00:00Z'



def get_stu_index():
	'''通过第一个issue，下载py103的学员索引'''
	url = 'https://api.github.com/repos/%s/%s/issues/1' % (REPO_OWNER, REPO_NAME)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url)
	result = json.loads(r.text)

	names = result["body"].split('|')
	ls = [name.strip() for name in names]

	VALUE = [('1','30'),('1','47'),('1','26'),('1','25')]
	AREA = ['BEIJING','CHANG','ZHU','OTHER']
	stu_list = {}
	i = 0
	j = len(ls)-1
	t = 0
	for (start,end) in VALUE:
	    m = ls.index(start, i, j)
	    n = ls.index(end, i, j)
	    
	    i = n + 6
	    stu_list[AREA[t]] = ls[m:i]
	    t = t + 1

	github_user = [] #github username of the students
	for area in AREA:
	    length = len(stu_list[area])
	    for i in range(1,length,7):
	        github_user.append(stu_list[area][i])
	return github_user # return list named github_user
	# print(github_user)
	# len(stu_list['BEIJING'])
	# print(stu_list['CHANG'])

payload1 = {'state':STATE,
			'since':TIME}	 
def list_task_issue_number():

	# url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
	#url = 'https://api.github.com/orgs/%s/issues' % (ORG_NAME)
# 	s = requests.session()
# 	s.auth = (USERNAME,PASSWORD)
# 	r = s.get(url,params = payload1)
# 	# print(r.headers)
# 	# r.headers["link"]

# # 	result = json.loads(r.text)
# # #	print(result)
# 	# ls = []
# # 	for x in result:
# # 		m = [x["url"],x["number"]]
# # 		ls.append(m)

# 	n = r.headers["Link"].split()
# 	print(n)
# 	ls = []
# 	while('rel = "next"' in n):
# 		# s = requests.session()
# 		# s.auth = (USERNAME,PASSWORD)
# 		# n = s.get(url, params = payload1)
# 		result = json.loads(r.text)

# 		for x in result:
# 			m = [x["url"],x["number"]]
# 			ls.append(m)

# 		start = n.index("<") + 1
# 		end = n.index(">")
# 		url = n[start:end]

	url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url,params = payload1)
	result = json.loads(r.text)
	ls = []
	for x in result:
		m = x["number"]
		ls.append(m)
	n = r.headers["Link"].split()
	while('rel = "next"' in n):
		start = n.index("<") + 1
		end = n.index(">")
		url = n[start:end]
		r = s.get(url,params=payload1)
		print(r.headers)
		result = json.loads(r.text)
		for x in result:
			m = x["numver"]
			ls.append(m)
		n = r.headers["Link"].split()

	return ls

r = list_task_issue_number()
print(r)

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
		if m in CHAP_NUMBER:
			dic["user"]["login"]
		ls.append(m)
	return ls


	如果title中包含有chap7,那么就把这个值赋给chap7_time
