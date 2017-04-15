import json
import requests
from flask import Flask, flash, redirect, render_template, request, session, abort,g
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *

import sqlite3
import datetime
from utils.const_value import DATABASE, REPO_OWNER, REPO_NAME,AREA,payload,payload1,payload2,TIME,LABEL,STATE,PAGE
import query_function as qf

engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)

List_history = []

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    '''login page'''
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # return "Hello Boss!  <a href='/logout'>Logout</a>"
        return render_template('index.html')
    # return render_template('index.html')

@app.route('/error')
def error():
    return "wrong"

@app.route('/login', methods=['POST'])
def do_admin_login():
    '''deal with login'''
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()

    if result:
        session['logged_in'] = True
        return home()
    else:
        print('wrong')
        flash('wrong password!')
        return error()
 
    # https://pythonspot.com/en/flask-web-forms/

@app.route("/logout")
def logout():
    '''deal with logout'''
    session['logged_in'] = False
    return home()

@app.route('/query', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.form['UserName']

        if r and request.form['query'] == '查询':
            s = qf.query_from_db('submit_issue', 'github_user_name', r)
            q = qf.query_from_db('issue_info', 'issue_creator',r)
            n = qf.query_from_db('stats_code','github_user_name',r)
            # print(s,type(s))

            count = 0
            for number in range(298):
                w = qf.query_from_db('issue_info','issue_num',number)
                # print(tuple(w))
                count += qf.count_issue(w,r)

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
            s = qf.static_performance()
            return render_template(PAGE, py103 = s)
        else:
            return render_template(PAGE)
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)