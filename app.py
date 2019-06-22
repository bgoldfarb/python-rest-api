from flask import Flask, jsonify


app = Flask(__name__)

stores = [
    {
        'name' : 'Good Store',
        'items' : [
            {
            'price' : 15.99
            }
        ]
    }
]

@app.route('/') #https://www.google.com/ Home page
def home():
    return "Hello World"

#POST - used to recieve data {name:}
#GET - used to send data back only 

#POST
@app.route('/store', methods=['POST'])
def createStore():
    pass

#GET
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

#POST
@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    pass

#GET
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

app.run(port=5000)