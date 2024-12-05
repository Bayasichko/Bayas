class Product:
	name = ''
	volume = 0
	price = 0
	amount = 0

	def __init__(self, name, volume, price, amount):
		self.name = name
		self.volume = volume
		self.price = price
		self.amount = amount

	def __str__(self):
		return f'''
Название : {self.name}
Объем: {self.volume}
Цена: {self.price}
Кол-во: {self.amount}
'''

product1 = Product('Coke', 0.5, 65, 30)
print(product1.__dict__)