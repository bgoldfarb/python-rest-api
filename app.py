from flask import Flask


app = Flask(__name__)

@app.route('/') #https://www.google.com/ Home page
def home():
    return "Hello World"


app.run(port=5000)