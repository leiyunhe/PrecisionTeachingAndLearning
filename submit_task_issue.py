#coding=utf-8
import json
import requests
from flask import Flask,request, render_template,g
import sqlite3
import datetime

app = Flask(__name__)

USERNAME = 'leiyunhe'
PASSWORD = 'Craney20150421'
CREATOR = 'leiyunhe'
TIME = '2017-01-01T00:00:00Z'
REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'
payload = {
			'since':TIME} # 每个函数传递的payload不同，因此需要修改，重新写成几个不同的payload,存在字典中，以备调用。
DATABASE = './database.db'
PAGE = 'index.html'
ISSUE_NUMBER_LIST = []

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

def submit_task_issue():
	'''返回用户ISSUE_NUMBER单元作业的提交时间、number,用于排序
	List comments on an issue
	DOC  https://developer.github.com/v3/issues/comments/
	'''
	url = 'https://api.github.com/repos/%s/%s/issues/%s/comments' % (REPO_OWNER, REPO_NAME,ISSUE_NUMBER)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url,params = payload)
	result = json.loads(r.text)
	ls = []
	for x in result:
		m = [x["url"],x["created_at"]]
		ls.append(m)
	return ls


ISSUE_NUMBER_LIST = []

def 

def insert_into_db(name,chap1_time,chap2_time,chap3_time,chap4_time,chap5_time,chap6_time,chap7_time):
	'''从API获取数据，并保存到数据库中'''
	c = get_db().cursor()
	# qttime = datetime.date.today()
	# city_name = city
	c.execute("INSERT INTO submit_issue VALUES (?,?,?,?,?,?,?,?)",(name,chap1_time,chap2_time,chap3_time,chap4_time,chap5_time,chap6_time,chap7_time))
	get_db().commit()





@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.form['InputCity']

		if r and request.form['query'] == '查询':
			t = query_realtime(r)
			insert_into_db(r, t[r][0], t[r][1])
			s = query_from_db(r)		
			return render_template(PAGE, result = s)
		elif r and request.form['update'] == '更正':
			c = get_db().cursor()
			d = r.split(" ")
			q = query_from_db(d[0])

			if q and (d[1] in UPDATE_DIC):
				c.execute("UPDATE qw SET weather= ? WHERE city_name = ?" , (str(d[1]),str(d[0])))
				get_db().commit()
				s = q
			else:
				s = ["请输入正确的天气情况：如晴，雪，雨，阴"]

			return render_template(PGAE, result = s)	
		else:
			return render_template(PAGE)		

	else:
		if request.args.get('help') == '帮助':
			s = documentation("README.md").splitlines()
			return render_template(PAGE, result = s)
		elif request.args.get('history') == '历史':
			s = documentation("log.txt").splitlines()
			return render_template(PAGE, result = s)
		else:
			return render_template(PAGE)

if __name__ == '__main__':
	

	with app.app_context():
		app.run(debug=True)