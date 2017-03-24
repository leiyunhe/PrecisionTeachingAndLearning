

def get_all_issues():
    ls = traverse_pages()
    issue_ls = []
    for page in ls:
        for x in page:
            m = [x["title"],x["number"]]
            issue_ls.append(m)
    return issue_ls

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
		m = [x["user"]["login"],x["created_at"],x["body"]]		
		ls.append(m)
	return ls
	print(ls)
###################################

def get_user_issue():
    ls = traverse_pages()
    issue_ls = []
    for page in ls:
        for x in page:
            m = [x["title"],x["number"]]
            issue_ls.append(m)
    return issue_ls	


def get_user_issue_comment(chap_num):
	issues = get_all_issues()
	for chap_num in ['ch1','ch2']:
		'chap%s_issues_list' % chap_num = 
		user_comment = {'user':{'chap1':num, 'chap2':num, 'chap3':num};}



