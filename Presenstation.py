class Apple:
	color = ""
	size = (0, 0)
	weight = 0
	count = 0
	origin = ""
	sort = ""

	def __init__(self, color, size, weight, count, origin, sort):
		self.color = color
		self.size = size
		self.weight = weight
		self.count = count
		self.origin = origin
		self.sort = sort

	def do_smile(self):
		print(f'Яблоко из {self.origin} сорта "{self.sort}" зловеще улыбнулась')

	def show_info(self):
		print(f"Размеры яблока сорта {self.sort} - {self.size[0]}см на {self.size[1]}")
		print(f"На складе {self.weight}кг яблок")
		print(f"На складе {self.count}штук яблок")
		print(f"Яблоки прибыли из {self.origin}")

apple_purple = Apple("Фиолетывый", (20, 10), 2, 15, "Чолдо", "Пурпл")
apple_red = Apple("Крастный", (15, 5), 5, 40, "Кызыл-кия", "Виктория")


apple_purple.do_smile()
apple_purple.show_info()