from bs4 import BeautifulSoup
import requests

def return_lines(url):	
	s = requests.session()
	r = s.get(url)
	html_doc = r.text

	soup = BeautifulSoup(html_doc, 'html.parser')
	# print(soup.prettify())
	f = soup.find('div',class_="file-info").text
	m = f.strip().split()
	return m[0]
url = 'https://github.com/leiyunhe/PrecisionTeachingAndLearning/blob/master/PrecisionTeachingV3/issue_creator.py'
r = return_lines(url)
print(r)