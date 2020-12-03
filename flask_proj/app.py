from flask import  Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name':'Kamal store',
        'item':[
            {
                'name':'T shirt',
                'price':8.5
            }
        ]
    },
    {
        'name':'Morgan store',
        'item':[
            {
                'name':'Panthi',
                'price':20.9
            }
        ]
    }
]

@app.route('/test/<name>')
def index(name):
    return '<h1> Hellooo {}! </h1>'.format(name)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'item' : request_data['item']
    }
    stores.append(new_store)
    return  jsonify(new_store) #'store created'

@app.route('/store/<string:store_name>/item', methods=['POST'])
def create_item(store_name):
    request_data = request.get_json()
    for store in stores:
        if store_name == store['name']:           
            store['item'].append(request_data)
            return  jsonify(request_data) #'item created'
    return 'store not in list'


@app.route('/store/<string:name>')
def get_store(name):
    for nm in stores:
        if nm['name'] == name:
            return 'store is exist'
    return 'store does not exist'

@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

app.run(port=8000)

