from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#Render a basic HTML Template in Jinja
def hello():
    return render_template('index.html')

@app.route('/profile')
def profile(): 
    return render_template('profile.html')

@app.route('/results')
def results(): 
    return render_template('results.html')

@app.route('/posting')
def posting(): 
    return render_template('posting.html')
#Test to show flask working
'''def hello_world():
    return 'Hello, World!'
'''