from flask import Flask, jsonify, request, render_template


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
    return render_template('index.html')

#POST - used to recieve data {name:}
#GET - used to send data back only 

#POST
@app.route('/store', methods=['POST'])
def createStore():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'no store found '})

#GET
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

#POST
@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message' : 'store not found'})

#GET
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items' : store['items']})
        return jsonify({'message' : 'items not found'})

app.run(port=5000)