from flask import Flask, request, render_template
#from RealtimeQuery import query_realtime, documentation, log, log_append
# from get_submit_time import
# import get_submit_time

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
	if request.method == 'POST':
		r = request.form['UserName']
		if r in get_stu_index():
			#pages = traverse_pages()
			# issues = get_all_issues()
			# ISSUE_NUMBER
			# submit_task_issue(ISSUE_NUMBER)
			# area = '长三角大区' 
			# issue = ['长三角大区ch7任务提交处','264']
			# get_issue_number(area,issue)
			# get_issue_comments_by_chap()
			# s = issue_comment_time
			s = 'numver'
			return render_template('index.html', result = s)
		
		else:
			return render_template('index.html')

	else:
		return render_template('index.html')

if __name__ == '__main__':

	app.run(debug = True)