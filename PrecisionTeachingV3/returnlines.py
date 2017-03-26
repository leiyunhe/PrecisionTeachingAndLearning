from bs4 import BeautifulSoup
import requests
import json

def return_lines(url):	
	s = requests.session()
	r = s.get(url)
	html_doc = r.text

	soup = BeautifulSoup(html_doc, 'html.parser')
	# print(soup.prettify())
	f = soup.find('div',class_="file-info").text
	m = f.strip().split()
	return m[0]
# url = 'https://github.com/leiyunhe/PrecisionTeachingAndLearning/blob/master/PrecisionTeachingV3/issue_creator.py'
# r = return_lines(url)
# print(r)

def get_file(url, suffix):
# GET /repos/:owner/:repo/contents/:path
	s = requests.session()
	r = s.get(url)
	result = json.loads(r.text)
	# print(result)
	ls = []
	print(result['path'])
	if list(result['path'])[-3:] == list(suffix):
		ls.append(result['_links']['html'])
	return ls

url = 'https://api.github.com/repos/leiyunhe/PrecisionTeachingAndLearning/contents/PrecisionTeachingV3'
file_ls = get_file(url,'.py')
for file in file_ls:
	m = return_lines(file)
	print(m)
