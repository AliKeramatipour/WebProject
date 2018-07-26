from flask import Flask, url_for, request, Response, jsonify, render_template

app = Flask(__name__)
"""localhost/?q=text"""


@app.route('/')
def search_1():
	return render_template('home.html')

@app.route('/login', methods=['POST'])
def search_function():
	print(">>> ", request.form)
	return render_template('index.html', data=request.form['firstname'] + request.form['lastname'])

if __name__ == '__main__':
	app.run(port=5002)