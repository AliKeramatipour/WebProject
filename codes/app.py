from flask import Flask, url_for, request, Response, jsonify, render_template, redirect, session
import requests
import json

app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')
def home():
	if 'username' in session :
		return render_template('index.html', data=session['username'] )
	else :
		return render_template('home.html')

@app.route('/login', methods=['POST'])
def search_function():
	if request.form['username'] == 'admin' and request.form['password'] == '1234' :
		session['username'] = request.form['username']
		return render_template('main.html')
	else :
		return redirect("", code=302)

@app.route('/search', methods=['GET'])
def search_wikipedia():
	search_string = request.args['query']
	json_format = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&exsentences=2&explaintext=&format=json&redirects=&formatversion=2&titles=' + search_string).content
	array = json.loads(json_format)
	return array['query']['pages'][0]['extract']

if __name__ == '__main__':
	app.run(port=5002)
