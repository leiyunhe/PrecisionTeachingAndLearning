import json
import requests
from flask import g
import sqlite3

USERNAME = 'leiyunhe'
PASSWORD = 'Craney20150421'

REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'

LABEL = 'task'
STATE = 'all'

TIME = '2017-01-01T00:00:00Z'
AREA = {'长三角大区','珠三角大区','北京大区','其他地区'}
DATABASE = './database.db'
PAGE = 'index.html'

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
	# print(result)
	ls = []
	for x in result:
		# print(x)
		# m = [x["url"],x["created_at"],x["user"]]
		# m = [x["url"],x["created_at"],x["user"]["login"]]
		m = [x["user"]["login"],x["created_at"]]		
		ls.append(m)
	return ls
	print(ls)

# sumbmit_task_issue('264')


def traverse_pages():
    '''travesing all pages, return a list including all pages'''
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    #url = 'https://api.github.com/orgs/%s/issues' % (ORG_NAME)
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
	# print(area,issues)
	issue_number = {'ch1': None, 'ch2': None, 'ch3': None, 'ch4': None, 'ch5': None, 'ch6': None, 'ch7': None}
	for issue in issues:
		for chapter in issue_number.keys():
			# print(chapter)
			if area in issue[0] and chapter in issue[0]:
				# print(area,chapter)
				issue_number[chapter] = issue[1]
				# print(issue_number[chapter])
	return issue_number


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     db.row_factory = sqlite3.Row
#     return db

# def query_db(query, args=(), one=False):
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv

# def query_from_db(name):
# 	'''通过用户github名称，从数据库查询用户每个单元作业的提交时间'''
# 	r = query_db('select * from submit_issue where github_user_name = ?',
# 	                [name], one=True)
# 	if r is None:
# 	    print('No such user')
# 	else:
# 	    print(r)
# 	return r

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

def insert_into_db():
	'''update db from API'''
	# c = get_db().cursor()

	ls_issues = get_all_issues()
	for area in AREA:
		#print(area)
		# for issue in ls_issues:
		# 	print(issue)
		ls_area_issue_numbers = get_issue_number(area, ls_issues)
			# print(ls_area_issue_numbers)
		for  ch_num  in ls_area_issue_numbers.keys():
			issue_num = ls_area_issue_numbers[ch_num]
			print(issue_num)
			# try:

			# print('issue_num: %s, issue_num: %r' % (type(issue_num), issue_num))
			if issue_num:
				comments =  submit_task_issue(issue_num)
			# 	break
			# except:
				

				for comment in comments:
					username = comment[0]
					created_at_time = comment[1]
					# chap1_time = chap2_time = chap3_time = chap4_time = chap5_time = chap6_time = chap7_time = 0
					if 'ch1' in ch_num:						
						# chap1_time = created_at_time
						UPDATE submit_issue SET chap1_time = created_at_time WHERE github_user_name = username
					elif 'ch2' in ch_num:
						UPDATE submit_issue SET chap2_time = created_at_time WHERE github_user_name = username
					elif 'ch3' in ch_num:
						UPDATE submit_issue SET chap3_time = created_at_time WHERE github_user_name = username
					elif 'ch4' in ch_num:
						UPDATE submit_issue SET chap4_time = created_at_time WHERE github_user_name = username
					elif 'ch5' in ch_num:
						UPDATE submit_issue SET chap5_time = created_at_time WHERE github_user_name = username
					elif 'ch6' in ch_num:
						UPDATE submit_issue SET chap6_time = created_at_time WHERE github_user_name = username
					else:
							# update_col = 'chap7_time'
						UPDATE submit_issue SET chap7_time = created_at_time WHERE github_user_name = username			

				# UPDATE submit_issue SET chap1_time=chap1_time chap2_time=chap2_time chap3_time=chap3_time chap4_time=chap4_time chap5_time=chap5_time chap6_time=chap6_time chap7_time=chap7_time WHERE github_user_name = username
			# conn.execute("INSERT INTO submit_issue VALUES (?,?,?,?,?,?,?,?)",(username,chap1_time,chap2_time,chap3_time,chap4_time,chap5_time,chap6_time,chap7_time))
	# get_db().commit()


# if __name__ == "__main__":
# 	insert_into_db()



conn = sqlite3.connect('databasetest.db')
print("Opened database successfully")

# conn.execute('CREATE TABLE qw (qttime TEXT, city_name TEXT, weather TEXT, temperature TEXT)')
conn.execute('CREATE TABLE submit_issue (github_user_name TEXT, chap1_time TEXT, chap2_time TEXT, chap3_time TEXT, chap4_time TEXT, chap5_time TEXT, chap6_time TEXT,chap7_time TEXT)')
print("Table created successfully")


insert_into_db()
for row in conn.execute('SELECT * FROM submit_issue ORDER by github_user_name'):
	print(row)

cur = conn.cursor()
print(cur.fetchall())

conn.close()