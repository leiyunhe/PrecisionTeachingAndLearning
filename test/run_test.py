#coding=utf-8
import json
import requests
from flask import Flask,request, render_template,g
import sqlite3
import datetime
import get_submit_time

app = Flask(__name__)

USERNAME = 'leiyunhe'
PASSWORD = 'he18801730209'
CREATOR = 'leiyunhe'
TIME = '2017-01-01T00:00:00Z'
REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'
payload = {
			'since':TIME} # 每个函数传递的payload不同，因此需要修改，重新写成几个不同的payload,存在字典中，以备调用。
DATABASE = './database.db'
PAGE = 'index.html'

AREA = {'长三角大区','珠三角大区','北京大区','其他地区'}

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def query_from_db(name):
	'''通过用户github名称，从数据库查询用户每个单元作业的提交时间'''
	r = query_db('select * from submit_issue where github_user_name = ?',
	                [name], one=True)
	if r is None:
	    print('No such user')
	else:
	    print(r)
	return r

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def insert_into_db():
	c = get_db().cursor()

	ls_issues = get_submit_time.get_all_issues()
	for area in AREA:
		#print(area)
		# for issue in ls_issues:
		# 	print(issue)
		ls_area_issue_numbers = get_submit_time.get_issue_number(area, ls_issues)
			# print(ls_area_issue_numbers)
		for  ch_num  in ls_area_issue_numbers.keys():
			issue_num = ls_area_issue_numbers[ch_num]
			# print(issue_num)
			# print('issue_num: %s, issue_num: %r' % (type(issue_num), issue_num))
			comments =  get_submit_time.submit_task_issue(issue_num)

			for comment in comments:
				username = comment[0]
				created_at_time = comment[1]
				# chap1_time = chap2_time = chap3_time = chap4_time = chap5_time = chap6_time = chap7_time = 0
				if 'ch1' in ch_num:						
					chap1_time = created_at_time
				elif 'ch2' in ch_num:
					chap2_time = created_at_time
				elif 'ch3' in ch_num:
					chap3_time = created_at_time
				elif 'ch4' in ch_num:
					chap4_time = created_at_time
				elif 'ch5' in ch_num:
					chap5_time = created_at_time
				elif 'ch6' in ch_num:
					chap6_time = created_at_time
				else:
						# update_col = 'chap7_time'
					chap7_time = created_at_time			

					# UPDATE submit_issue SET update_col = created_at_time WHERE name = username
			c.execute("INSERT INTO submit_issue VALUES (?,?,?,?,?,?,?,?)",(username,chap1_time,chap2_time,chap3_time,chap4_time,chap5_time,chap6_time,chap7_time))
	get_db().commit()


@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.form['Input']

		if r and request.form['query'] == '查询':
			s = query_from_db(r)
			List_history.append(s)		
			return render_template(PAGE, result = s)
		else:
			s = '''请AIMinder Py103学员输入GitHub用户名，进行查询'''
			return render_template(PAGE, result = s)		

	else:
		if request.args.get('help') == 'help':
			s = '''AIMinder Py103学员输入GitHub用户名，查询个人提交作业的情况'''
			return render_template(PAGE, result = s)
		elif request.args.get('history') == 'history':
			s = List_history
			return render_template(PAGE, result = s)
		else:
			return render_template(PAGE)

if __name__ == '__main__':
	List_history = []
	
	with app.app_context():
		insert_into_db()
		app.run(debug=True)