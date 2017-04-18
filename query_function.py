#coding=utf-8
import json
import requests
from flask import Flask,request, render_template,g
import sqlite3
import datetime
from utils.const_value import DATABASE, REPO_OWNER, REPO_NAME,AREA,payload,payload1,payload2,TIME,LABEL,STATE,PAGE
# several query functions
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


def create_table(cursor, table,columns):
	try:
		cursor.execute('CREATE TABLE %s %s' % (table,columns))
	except:
		print("Table exits!")
		cursor.execute('DELETE FROM %s' % table)
		print("Table has been deleted!")
	finally:
		print("Table created successfully!")