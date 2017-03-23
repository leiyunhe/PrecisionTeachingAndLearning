#coding=utf-8
import json
import requests
from flask import Flask,request, render_template,g
import sqlite3
import datetime
from utils.const_value import REPO_OWNER, REPO_NAME, USERNAME,PASSWORD,AREA,payload,payload1,payload2,TIME,DATABASE,LABEL,STATE,PAGE

app = Flask(__name__)
List_history = []


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
			s = query_from_db(r)
			# print(s,type(s))
			List_history.append(tuple(s))		
			return render_template(PAGE, result = s)
		else:
			s = ['请AIMinder Py103学员输入GitHub用户名，进行查询']
			return render_template(PAGE, result = s)		

	else:
		if request.args.get('button') == 'help':
			s = ['AIMinder Py103学员输入GitHub用户名，查询个人提交作业的情况']
			return render_template(PAGE, help = s)
		elif request.args.get('button') == 'history':
			s = List_history
			return render_template(PAGE, history = s)
		elif request.args.get('button') == 'Py103':
			# s = []
			# for item in fetch_db():
			# 	s.append(item)
			# s[0] = fetch_db()
			# # s = fetch_db()
			s = static_performance()
			return render_template(PAGE, py103 = s)
		else:
			return render_template(PAGE)

if __name__ == '__main__':
	
	
	with app.app_context():
		# insert_into_db()
		app.run(debug=True)