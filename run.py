from flask import Flask, request, render_template
#from RealtimeQuery import query_realtime, documentation, log, log_append

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
	if request.method == 'POST':
		r = request.form['UserName']
		pose_question = ask_question_issue(r)
		if r:
			# pose_question = ask_question_issue("UserName")
			s = "your leanring:"
			return render_template('index.html', result = s)
		
		else:
			return render_template('index.html')

	else:
		if request.args.get('help') == 'help':
			s = '''please input your github user name,and check your perfomance in py103'''
			return render_template('index.html', result = s)
		elif request.args.get('history') == 'history':
			s = '''your hisroty is ...'''
			return render_template('index.html', result = s)
		else:
			return render_template('index.html')

if __name__ == '__main__':

	app.run(debug = True)