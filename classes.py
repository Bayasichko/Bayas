product1 = {
	'name': 'Coke',
	'volume': 0.5,
	'price': 65,
	'amount': 30
}

product2 = {
	'name': 'Piko',
	'volume': 1,
	'price': 125,
	'amount': 17
}

def purchase_product(product):
	product['amount'] -= 1

purchase_product(product1)
print(product1)