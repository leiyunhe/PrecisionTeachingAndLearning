from bs4 import BeautifulSoup
import requests
import json

def return_lines(url):	
	s = requests.session()
	s.auth = (USER,PASSWORD)
	r = s.get(url)
	html_doc = r.text
	print(html_doc)
	soup = BeautifulSoup(html_doc, 'html.parser')
	# print(soup.prettify())

	# f = soup.find('div',class_="file-info").text
	f = soup.find('div',class_="file-info")
	print(f)
	if f:
		f = f.text
		m = f.strip().split()
		return m[0]
# url = 'https://github.com/leiyunhe/PrecisionTeachingAndLearning/blob/master/PrecisionTeachingV3/issue_creator.py'
# r = return_lines(url)
# print(r)

def get_file(url):
# GET /repos/:owner/:repo/contents/:path
	s = requests.session()
	s.auth = (USER,PASSWORD)
	r = s.get(url)
	# print(r)
	result = json.loads(r.text)
	# print(result)
	ls = []
	for filename in result:
		print(filename)
		# print(filename['path'])
		if filename['path'][-3:] == '.py':
			filename['path']
			ls.append(filename['_links']['html'])
		else:
			pass
	# print(ls)
	return ls

# if __name__ == '__main__':
# 	'''get lines of .py in public repos
# 		succeed'''
# 	url = 'https://api.github.com/repos/leiyunhe/PrecisionTeachingAndLearning/contents/PrecisionTeachingV3'
# 	USER = 'yunhe.lei@gmail.com'
# 	PASSWORD = 'he18801730209'
# 	file_ls = get_file(url)
# 	num = 0
# 	for file in file_ls:
# 		# print(file,return_lines(file))
# 		num += int(return_lines(file))
# 	print(num)


# get lines of .py in repos forked from private repos in organization
def save_user_code_lines(USERNAME,CHAPTER):
	# url = 'https://api.github.com/leiyunhe/Py103/tree/master/Chap1/project'
	url = 'https://api.github.com/repos/%s/Py103/contents/%s/project' % (USERNAME,CHAPTER)
	# s = requests.session()
	# s.auth = (USERNAME,PASSWORD)
	file_ls = get_file(url)
	lines_sum = 0
	for file in file_ls:
		print(file,return_lines(file))
		# lines_ls.append(return_lines(file))
		m = return_lines(file)
		if m:
			lines_sum += int(m)
		# lines_sum += lines
	return lines_sum
USER = 'yunhe.lei@gmail.com'
PASSWORD = 'he18801730209'
r = save_user_code_lines('leiyunhe','Chap1')
print(r)



