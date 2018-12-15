from flask import Flask, jsonify, request
from db import DatabaseConnection

app = Flask(__name__)


@app.route('/products')
def get_products():
	db = DatabaseConnection()
	products = db.get_products()
	return jsonify({'products': products}), 200

@app.route('/products', methods=['POST'])
def add_product():
	info = request.get_json()
	product = info.get('product')
	purchace = info.get('purchace')
	resale = info.get('resale')
	stock = info.get('stock')

	db = DatabaseConnection()
	message = db.add_product(product, purchace, resale, stock)

	return jsonify({'message': message}), 201

@app.route('/modify', methods=['PATCH'])
def modify_product():
	info = request.get_json()
	product = info.get('product') # The product whose value we wish to change
	attribute = info.get('attribute') # The column name whose value we wish to change
	value = info.get('value') # The new value we wish to add

	db = DatabaseConnection()
	message = db.modify_product(product, attribute, value)

	return jsonify({'message': message}), 201

# Here we add a variable to our route
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
	db = DatabaseConnection()
	message = db.delete_product(id)

	return jsonify({'message': message})


if __name__ == '__main__':
	app.run(debug=True)