from bs4 import BeautifulSoup
import requests
import json

def return_lines(url):	
	s = requests.session()
	s.auth = (USER,PASSWORD)
	r = s.get(url)
	print(r)
	html_doc = r.text
	# print(html_doc)
	soup = BeautifulSoup(html_doc, 'html.parser')
	# print(soup.prettify())

	# f = soup.find('div',class_="file-info").text
	f = soup.find('div',class_="file-info")
	# print(f)
	if f:
		f = f.text
		m = f.strip().split()
		return m[0]

def get_file(url):
# GET /repos/:owner/:repo/contents/:path
	s = requests.session()
	s.auth = (USER,PASSWORD)
	r = s.get(url)
	print('get_file_test',r)
	result = json.loads(r.text)
	# print(result)
	ls = []
	for filename in result:
		# print(filename)
		# print(filename['path'])
		if filename['type'] == 'file' and filename['path'][-3:] == '.py':
			ls.append(filename['_links']['html'])
		elif filename['type'] == 'dir':
			url_dir = filename['_links']['self']
			get_file(url_dir)
		else:
			pass
	# print(ls)
	return ls

if __name__ == '__main__':
	'''get lines of .py in public repos
		succeed'''
	# url = 'https://api.github.com/repos/leiyunhe/PrecisionTeachingAndLearning/contents/PrecisionTeachingV3'
	url = 'https://api.github.com/repos/leiyunhe/Py103/contents/Chap1/project'
	USER = 'leiyunhe'
	PASSWORD = 'HE18801730209'
	file_ls = get_file(url)
	num = 0
	print(file_ls)
	for file_name in file_ls:
		m = return_lines(file_name)
		if m:
		# print(file,return_lines(file))
			num += int(m)
			print(m)
	print(num)


# get lines of .py in repos forked from private repos in organization
# def save_user_code_lines():
# 	# url = 'https://api.github.com/leiyunhe/Py103/tree/master/Chap1/project'
# 	url = 'https://api.github.com/repos/leiyunhe/Py103/contents/Chap1/project/1w-query.py'
# 	# s = requests.session()
# 	# s.auth = (USERNAME,PASSWORD)
# 	file_ls = get_file(url)
# 	lines_sum = 0
# 	for file in file_ls:
# 		print(file,return_lines(file))
# 		# lines_ls.append(return_lines(file))
# 		m = return_lines(file)
# 		if m:
# 			lines_sum += int(m)
# 		# lines_sum += lines
# 	return lines_sum


# r = save_user_code_lines()
# print(r)



