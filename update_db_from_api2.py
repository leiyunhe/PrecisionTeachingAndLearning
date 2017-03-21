import json
import requests
from flask import g
import sqlite3
from utils.const_value import REPO_OWNER, REPO_NAME, USERNAME,PASSWORD,AREA,payload,payload1,payload2,TIME,DATABASE,LABEL,STATE


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
	        github_user.append((stu_list[area][i],area))
	return github_user


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

def traverse_pages():
    '''travesing all pages, return a list including all pages'''
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    s = requests.session()
    s.auth = (USERNAME,PASSWORD)
    r = s.get(url,params = payload1)
    li = r.headers["Link"]
    next_url=li[(li.index("<") + 1):li.index(">")]
    result = json.loads(r.text)
    ls = []
    ls.append(result)      
    while True:
        r = s.get(next_url,params = payload1)
        result = json.loads(r.text)
        ls.append(result)
        link = r.headers['Link']
        if 'next' not in link:
            break
        next_url=link[(link.index("<") + 1):link.index(">")]
    return ls

def get_all_issues():
    ls = traverse_pages()
    issue_ls = []
    for page in ls:
        for x in page:
            m = [x["title"],x["number"]]
            issue_ls.append(m)
    return issue_ls

def get_issue_number(area, issues):
	'''	如果title中包含有chap7,那么就把这个值赋给chap7_time'''
	issue_number = {'ch1': None, 'ch2': None, 'ch3': None, 'ch4': None, 'ch5': None, 'ch6': None, 'ch7': None}
	for issue in issues:
		for chapter in issue_number.keys():
			if area in issue[0] and chapter in issue[0]:
				issue_number[chapter] = issue[1]
	return issue_number


def insert_into_db():
	'''update db from API'''
	ls_issues = get_all_issues()
	for area in AREA:
		ls_area_issue_numbers = get_issue_number(area, ls_issues)
		for  ch_num  in ls_area_issue_numbers.keys():
			issue_num = ls_area_issue_numbers[ch_num]
			print(issue_num)
			if issue_num:
				comments =  submit_task_issue(issue_num)

				for comment in comments:
					if 'https://github.com/' in comment[2]:
						if 'ch1' in ch_num:
							c.execute("UPDATE submit_issue SET chap1_time = ? WHERE github_user_name = ?", (comment[1],comment[0]))
						elif 'ch2' in ch_num:
							c.execute("UPDATE submit_issue SET chap2_time = ? WHERE github_user_name = ?", (comment[1],comment[0]))
						elif 'ch3' in ch_num:
							c.execute("UPDATE submit_issue SET chap3_time = ? WHERE github_user_name = ?", (comment[1],comment[0]))
						elif 'ch4' in ch_num:
							c.execute("UPDATE submit_issue SET chap4_time = ? WHERE github_user_name = ?", (comment[1],comment[0]))
						elif 'ch5' in ch_num:
							c.execute("UPDATE submit_issue SET chap5_time = ? WHERE github_user_name = ?", (comment[1],comment[0]))
						elif 'ch6' in ch_num:
							c.execute("UPDATE submit_issue SET chap6_time = ? WHERE github_user_name = ?", (comment[1],comment[0]))
						elif 'ch7' in ch_num:
							c.execute("UPDATE submit_issue SET chap7_time = ? WHERE github_user_name = ?", (comment[1],comment[0]))
						else:
							pass
					else:
						pass
					conn.commit()		


if __name__ == '__main__':
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()

	c.execute('CREATE TABLE submit_issue (github_user_name TEXT, area TEXT, chap1_time TEXT, chap2_time TEXT, chap3_time TEXT, chap4_time TEXT, chap5_time TEXT, chap6_time TEXT,chap7_time TEXT)')
	print("Table created successfully")

	for stu in get_stu_index():
		c.execute('INSERT INTO submit_issue (github_user_name, area) VALUES (?,?)',(stu[0],stu[1]))
	conn.commit()
	insert_into_db()

	for row in c.execute('SELECT * FROM submit_issue ORDER by github_user_name'):
		print(row)

	conn.commit()
	conn.close()