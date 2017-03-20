USERNAME = 'leiyunhe'
PASSWORD = 'he18801730209'
# CREATOR = 'leiyunhe'
TIME = '2017-01-01T00:00:00Z'
REPO_OWNER = 'AIMinder'
REPO_NAME = 'Py103'
payload = {'since':TIME} # 每个函数传递的payload不同，因此需要修改，重新写成几个不同的payload,存在字典中，以备调用。
DATABASE = './database2.db'
PAGE = 'index2.html'

# AREA = {'长三角','珠三角','北京','其他'}


# REPO_OWNER = 'AIMinder'
# REPO_NAME = 'Py103'

LABEL = 'task'
STATE = 'all'

# TIME = '2017-01-01T00:00:00Z'
AREA = ['北京','长三角','珠三角','其他']
# DATABASE = './database2.db'
# PAGE = 'index2.html'

payload1 = {'state':STATE,
			'since':TIME}	 

payload2 = {'labels': LABEL,
			'state': STATE}

# DATABASE = './database2.db'