import json
import requests

USERNAME = 'leiyunhe'
PASSWORD = 'Craney20150421'

CREATOR = 'leiyunhe'
TIME = '2017-01-01T00:00:00Z'

REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'

# 每个函数传递的payload不同，因此需要修改，重新写成几个不同的payload,存在字典中，以备调用。
payload = {
			'since':TIME}

def ask_question_issue():
	'''The number of issues students create 
	List issues  GET /orgs/:org/issue
	Parameters:
		filter:assigned,created, mentioned,subscribed,all
		state:open,closed,all
		labels
		sort
		direction
		since:YYYY-MM-DDTHH:MM:SSZ
	'''
	url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
	s = requests.session()

	s.auth = (USERNAME,PASSWORD)
	r = s.get(url, params = payload)
	result = json.loads(r.text)

	ls = []
	
	for i in range(len(result)):
		issue_url = result[i]["url"]
		issue_number = result[i]["number"]
		ls[i] = (issue_url,issue_number)
	return ls

	# ls[i] = (issue_id,issue_number)

	# print(ls)
	# return ls
print(ask_question_issue())

def submit_task_issue():
	'''record the time when users submit their program, return the saved sort
	DOC  https://developer.github.com/v3/issues/comments/
	'''
	url = 'https://api.github.com/repos/%s/%s/issues/%s/comments' % (REPO_OWNER, REPO_NAME,ISSUE_NUMBER)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url,params = payload)
	result = json.loads(r.text)

	ls = []
	# return the url of comment and created_at 
	comment_url = result[0]["url"]
	conment_created_at = result[0]["created_at"]
	ls.append(comment_url,conment_created_at)
	return ls

def interaction():
	'''answer questions when the issue is created by their peers. The number of @username
	GET 
	'''

def reaction_for_issue_comment():
	'''List reactions for an issue comment
	GET /repos/:owner/:repo/issues/comments/:id/reactions
	'''
	


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

