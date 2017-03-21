USERNAME = 'leiyunhe'
PASSWORD = 'he18801730209'
TIME = '2017-01-01T00:00:00Z'
REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'

DATABASE = './database2.db'
PAGE = 'index2.html'

LABEL = 'task'
STATE = 'all'

AREA = ['北京','长三角','珠三角','其他']

payload = {'since':TIME}
payload1 = {'state':STATE,
			'labels': LABEL,
			'since':TIME}	 

payload2 = {'labels': LABEL,
			'state': STATE}
