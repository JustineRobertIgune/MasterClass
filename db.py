import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseConnection:
	def __init__(self):
		self.connection = psycopg2.connect(
                dbname='', user='', host='localhost', password='', port='5432'
            )

		print('Database connected.')
		self.connection.autocommit = True
		self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

		create_supermarket_table = 'CREATE TABLE IF NOT EXISTS supermarket(id SERIAL PRIMARY KEY, product TEXT, purchace_price INT, resale_price INT, stock INT);'
		self.cursor.execute(create_supermarket_table)

	def add_product(self, product, purchace, resale, stock):
		insert = f"""INSERT INTO supermarket(product, purchace_price, resale_price, stock) VALUES('{product}', {purchace}, {resale}, {stock});"""
		self.cursor.execute(insert)
		return 'Successfully added'

	def get_products(self):
		query = 'SELECT * FROM supermarket;'
		self.cursor.execute(query)
		products = self.cursor.fetchall()
		return products

	def modify_product(self, product, attribute, value):
		query = f"""UPDATE supermarket SET {attribute}='{value}' WHERE product='{product}'"""
		self.cursor.execute(query)
		return 'Updated successfully'

	def delete_product(self, id):
		query = f"""DELETE FROM supermarket WHERE id={id}"""
		self.cursor.execute(query)
		return 'Deleted successfully'

if __name__ == '__main__':
	db = DatabaseConnection()