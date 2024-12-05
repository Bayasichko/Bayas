
class Device:
	__is_working = False

	def start_switchness(self, is_working):
		if self.__is_working:
			print('Устройство уже включено.')
		else:
			self.__is_working = True
			print('Устройство включилось')

	def stop_switchness(self, is_working):
		if not self.__is_working:
			print('Устройство уже выключено')
		else:
			self.__is_working = False
			print('Устройство выключилось')

	def start(self):
		start_switchness()

	def stop(self):
		stop_switchness()

	def display(self):
		if self.__is_working:
			print('Устройство работает')
		else:
			print('Устройство не работает')


class ArithmeticProcessor(Device):
	@staticmethod
	def calculate(x, y):
		print('Устройство начало издавать страшные звуки и посчитало', x + y)


machine = Device()
machine.is_working()
ArithmeticProcessor.calculate(3, 4)









