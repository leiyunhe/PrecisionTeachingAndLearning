TIME = '2016-12-20T00:00:00Z'
REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'
DATABASE = 'database'
PAGE = 'index.html'

LABEL = 'task'
STATE = 'all'

AREA = ['北京','长三角','珠三角','其他']

payload = {'since':TIME}
payload1 = {'state':STATE,
			'labels': LABEL,
			'since':TIME}	 

payload2 = {'labels': LABEL,
			'state': STATE}
payload5 = {'state':STATE,
            'since':TIME}