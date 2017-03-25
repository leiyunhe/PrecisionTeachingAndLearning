#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
from flask import g
import sqlite3
# # from utils.const_value import REPO_OWNER, REPO_NAME, USERNAME,PASSWORD,AREA,payload,payload1,payload2,TIME,DATABASE,LABEL,STATE
# from utils.const_value import DATABASE, REPO_OWNER, REPO_NAME, AREA,payload,payload1,payload2,TIME,LABEL,STATE
# from login import login

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


def get_issue_comment(ISSUE_NUMBER):


def get_user_issue_comment():
	comment_num = {}
	issues = get_all_issues()
	for issue in issues:
		for number in issue:
			comments = submit_task_issue(number)
			for comment in comments:
				if username in comment:
					comment_num[username] += 1
	return comment_num

if __name__ == '__main__':

	argv = login.login()
	USERNAME = argv[0]
	PASSWORD = argv[1]

	conn = sqlite3.connect(DATABASE_STATS)
	c = conn.cursor()

	c.execute('CREATE TABLE comment_stats (github_user_name TEXT, area TEXT, chap1_comment TEXT, chap2_comment TEXT, chap3_comment TEXT, chap4_comment TEXT, chap5_comment TEXT, chap6_comment TEXT,chap7_comment TEXT)')
	print("Table created successfully")

	for stu in get_stu_index():
		c.execute('INSERT INTO comment_stats (github_user_name, area) VALUES (?,?)',(stu[0],stu[1]))
	conn.commit()



	for row in c.execute('SELECT * FROM comment_stats ORDER by github_user_name'):
		print(row)

	conn.commit()
	conn.close()



def get_user_issue_comment(chap_num):
	issues = get_all_issues()
	for chap_num in ['ch1','ch2']:
		'chap%s_issues_list' % chap_num = 
		user_comment = {'user':{'chap1':num, 'chap2':num, 'chap3':num};}



