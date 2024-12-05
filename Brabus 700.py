class Brabus:
	mark = 0
	price = 0
	max_speed = 0
	power = 0
	manufactory = 0
	color = ""

	def __init__(self, mark, price, max_speed, power, manufactory, color):
		self.mark = mark
		self.price = price
		self.max_speed = max_speed
		self.power = power
		self.manufactory = manufactory
		self.color = color

	def goal(self):
		print(f"")

brabus_700 = Brabus('700', '200')
