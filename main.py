from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import insert_data_db
from functions import get_data

app =  Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route("/get-products", methods=['GET'])
def get_products():
    data = get_data()
    # print(data)
    return jsonify({
        "products": data
    })
    

@app.route("/send-data", methods=['POST'])
def send_data():
    data = request.get_json()
    # print(data)
    for item in data:
        title = item.get('title')
        price = item.get('price')
        link = item.get('link')
        image = item.get('image')
        insert_data_db(title, price, link, image)
    return jsonify({'message': 'Data received successfully!'})

if __name__ == '__main__':  
    app.run(debug=True, host="0.0.0.0")