#coding=utf-8
import json
import requests
from flask import Flask,request, render_template,g
import sqlite3
import datetime
from utils.const_value import DATABASE, REPO_OWNER, REPO_NAME,AREA,payload,payload1,payload2,TIME,LABEL,STATE,PAGE

app = Flask(__name__)
List_history = []


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # db = g._database = sqlite3.connect(DATABASE)

    #db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    # print(rv)
    cur.close()
    return (rv[0] if rv else None) if one else rv

def query_from_db(table, index, value):
	'''通过用户github名称，从数据库查询用户每个单元作业的提交时间'''
	ls = []
	r = query_db('select * from %s where %s = ?' % (table, index),
	                [value], one=False)
	if r is None:
	    print('No such user')
	else:
	    # r = ls.append(r)
	    # for item in r:
	    # 	print(item)
	    print(r)
	return r

def static_performance():
	static = {}
	for area in AREA:
		static[area] = {}
	for district in AREA:
		for column in ['chap1_time','chap2_time','chap3_time','chap4_time','chap5_time','chap6_time','chap7_time']:
			ls = []
			for row in get_db().execute('SELECT * FROM submit_issue WHERE area = ? and %s != "None"' % column ,(district,)):
				ls.append(row)
			static[district][column] = len(ls)
	return static

def issue_stats(username):
	ls = []
	for row in get_db().execute('SELECT * FROM issue_info WHERE issue_creator = ?' % (username,)):
		ls.apend(tuple(row))

def count_issue(data,value):
	num =0
	for comment in data:
		if value in comment[1]:
			num += 1
		s = comment[3].split(",")
		for item in s:
			if value in item:
				num += 1
	return num

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.form['UserName']

		if r and request.form['query'] == '查询':
			s = query_from_db('submit_issue', 'github_user_name', r)
			q = query_from_db('issue_info', 'issue_creator',r)
			n = query_from_db('stats_code','github_user_name',r)
			# print(s,type(s))

			count = 0
			for number in range(298):
				w = query_from_db('issue_info','issue_num',number)
				# print(tuple(w))
				count += count_issue(w,r)

			List_history.append((tuple(s),tuple(q),tuple(n)))	
			return render_template(PAGE, result = (s,q,n,count))
		else:
			s = ['请AIMinder Py103学员输入GitHub用户名，进行查询']
			return render_template(PAGE, help = s)		

	else:
		if request.args.get('button') == 'help':
			s = ['AIMinder Py103学员输入GitHub用户名，查询个人提交作业的情况']
			return render_template(PAGE, help = s)
		elif request.args.get('button') == 'history':
			s = List_history
			return render_template(PAGE, history = s)
		elif request.args.get('button') == 'Py103':
			s = static_performance()
			return render_template(PAGE, py103 = s)
		elif request.args.get('button') =='长三角':
			shanghai = query_from_db('submit_issue','area', '长三角')
			return render_template(PAGE, area_shanghai = shanghai)
		elif request.args.get('button') =='北京':
			beijing = query_from_db('submit_issue','area', '北京')
			return render_template(PAGE, area_beijing = beijing)
		else:
			return render_template(PAGE)

if __name__ == '__main__':
	
	with app.app_context():
		app.run(debug=True)