from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#Render a basic HTML Template in Jinja
def hello():
    return render_template('profile.html')
#Test to show flask working
'''def hello_world():
    return 'Hello, World!'
'''