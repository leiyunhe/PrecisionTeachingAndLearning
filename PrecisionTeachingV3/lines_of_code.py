
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
# from flask import g
# import sqlite3
# from utils.const_value import REPO_OWNER, REPO_NAME, USERNAME,PASSWORD,AREA,payload,payload1,payload2,TIME,DATABASE,LABEL,STATE
# from utils.const_value import DATABASE, REPO_OWNER, REPO_NAME, AREA,payload,payload1,payload2,TIME,LABEL,STATE
# from login import login

REPO_OWNER = 'leiyunhe'
REPO_NAME = 'Py103'
USERNAME = 'yunhe.lei@gmail.com'
PASSWORD = 'he18801730209'

# url = 'https://api.github.com/repos/%s/%s/issues/1' % (REPO_OWNER, REPO_NAME)
# 	s = requests.session()
# 	s.auth = (USERNAME,PASSWORD)
# 	r = s.get(url)
# 	result = json.loads(r.text)

# 	names = result["body"].split('|')

def stat_lines_of_code():
	'''add and deletion'''
	url = 'https://api.github.com/repos/%s/%s/stats/code_frequency' % (REPO_OWNER, REPO_NAME)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url)
	result = json.loads(r.text)
	print(result[0])

	# s = requests.session()
	# s.auth = (USERNAME,PASSWORD)
	# r = s.get(url)
	# result = json.loads(r.text)

# stat_lines_of_code()

def get_stat():
	'''stats of repo'''
	url = 'https://githubstats.com/%s/%s' % (REPO_OWNER, REPO_NAME)
	s = requests.session()
	s.auth = (USERNAME,PASSWORD)
	r = s.get(url)
	# result = json.loads(r.text)
	print(r)





