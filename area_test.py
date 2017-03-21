from utils.const_value import REPO_OWNER, REPO_NAME, USERNAME,PASSWORD,AREA,payload,payload1,payload2,TIME,DATABASE,LABEL,STATE
import sqlite3

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

for row in c.execute('SELECT COUNT(area) FROM submit_issue  WHERE area = "长三角" ORDER by github_user_name'):
	print(row)


for row in c.execute('SELECT COUNT(area) FROM submit_issue  WHERE area = "长三角"'):
	print(row)


# for row in c.execute('SELECT COUNT(area, chap1_time) FROM submit_issue  WHERE area = "珠三角" and chap1_time !="None"'):
# 	print(row)

# 长三角chap1的数据有问题。
# print("长三角chap1")
# for row in c.execute('SELECT * FROM submit_issue WHERE area = "长三角" and chap2_time != "None"'):
# 	print(row)

# print("珠三角chap1")
# for row in c.execute('SELECT * FROM submit_issue WHERE area = "珠三角" and chap1_time != "None"'):
# 	print(row)

# print("珠三角chap7")
# # 例如，大猫的chap1不能抓取。因为使用了外部博客链接。没有使用GitHub仓库链接
# for row in c.execute('SELECT * FROM submit_issue WHERE area = "珠三角" and chap7_time != "None"'):
# 	print(row)

for d in ['长三角','珠三角','北京','其他']:
	for chap_num in ['chap1_time','chap2_time','chap3_time','chap4_time','chap5_time','chap6_time','chap7_time']:
		ls = []
		for row in c.execute('SELECT * FROM submit_issue  WHERE area = ? and ? != "None"',(d,chap_num)):
			ls.append(row)
		print(d,chap_num,len(ls))


conn.commit()
conn.close()


