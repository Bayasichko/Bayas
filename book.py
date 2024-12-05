class Book:
	name = ''
	author = ''
	description = ''
	amount_of_pages = 0
	amount_of_paragraphs = 0
	quantity_in_stock = 0
	price = 0

	def __init__(self, name, author, description, amount_of_pages, amount_of_paragraphs, quantity_in_stock, price):
		self.name = name
		self.author = author
		self.description = description
		self.amount_of_paragraphs = amount_of_paragraphs
		self.amount_of_pages = amount_of_pages
		self.quantity_in_stock = quantity_in_stock
		self.price = price

	def __str__(self):
		return f'''
	Название книги: {self.name}
	Автор книги: {self.author}
	Описание книги: {self.description}
	Количество страниц: {self.amount_of_pages}
	Количество параграфов: {self.amount_of_paragraphs}
	Кол-во на складе: {self.quantity_in_stock}
	Цена: {self.price}
	'''


product1 = Book('bayas', 'asdfd', 'asd', 234, 234, 234, 234)
print(product1.__str__())