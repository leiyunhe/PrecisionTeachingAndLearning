#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
# from flask import g
# import sqlite3
# # from utils.const_value import REPO_OWNER, REPO_NAME, USERNAME,PASSWORD,AREA,payload,payload1,payload2,TIME,DATABASE,LABEL,STATE
# from utils.const_value import DATABASE, REPO_OWNER, REPO_NAME, AREA,payload,payload1,payload2,TIME,LABEL,STATE


# def get_stu_index():
# 	'''通过第一个issue，下载py103的学员索引'''
# 	url = 'https://api.github.com/repos/%s/%s/issues/1' % (REPO_OWNER, REPO_NAME)
# 	s = requests.session()
# 	s.auth = (USERNAME,PASSWORD)
# 	r = s.get(url)
# 	result = json.loads(r.text)

# 	names = result["body"].split('|')
# 	ls = [name.strip() for name in names]

# 	VALUE = [('1','30'),('1','47'),('1','26'),('1','25')]
# 	stu_list = {}
# 	i = 0
# 	j = len(ls)-1
# 	t = 0
# 	for (start,end) in VALUE:
# 	    m = ls.index(start, i, j)
# 	    n = ls.index(end, i, j)
	    
# 	    i = n + 6
# 	    stu_list[AREA[t]] = ls[m:i]
# 	    t = t + 1

# 	github_user = [] #github username of the students
# 	for area in AREA:
# 	    length = len(stu_list[area])
# 	    for i in range(1,length,7):
# 	        github_user.append((stu_list[area][i],area))
# 	return github_user

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == '<tbody>':
        	print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        if tag == '</tbody>':
        	print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

    def return_filename(data):
    	if '<div class = "file_wrap">' in data:
    		if '<td class = "content">' in data:
    			print("caution:get content")
    			print(self.handle_data)

# parser = MyHTMLParser()
# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')


def get_repo_code_page():
	'''target: get the file tree of repo'''
	url = 'https://github.com/leiyunhe/learngit/tree/master'
	s = requests.session()
	# s.auth = (USERNAME,PASSWORD)
	r = s.get(url)
	# print(r)  # response 200
	return r.text
	# result = json.loads(r.text)
	# print(result)

raw_data = get_repo_code_page()
parser = MyHTMLParser()
parser.feed(raw_data)