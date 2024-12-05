class BankAccount:
	owner = ''
	__balance = ''
	__currency = 'som'
	__operations_history = []
	has_credits = False

	def __init__(self, owner, balance, currency, operations_history, has_credits):
		self.owner = owner
		self.__balance = balance
		self.__currency = currency
		self.__operations_history = operations_history
		self.has_credits = has_credits

	def __bayas(self):
		pass

	def add_to_balance(self, new_sum):
		if type(new_sum) is int:
			if 0 < new_sum < 25000:
				self.__balance += new_sum
				self.__add_history('Пополнение', new_sum)

	def withdraw(self, new_sum):
		if type(new_sum) is int:
			if 0 < new_sum < 25000:
				self.__balance -= new_sum
				self.__add_history('Снятие', new_sum)

	def __add_history(self, type, sum):
		self.__operations_history.append(
			{
				'type': type,
				'sum': sum
			}
		)
	def display_history(self):
		for i in self.__operations_history:
			print(f'Тип: {i['type']}, Сумма: {i['sum']}')

	def display_balance(self):
		print(f'Баланс: {self.__balance}{self.__currency}')


ba_bayas = BankAccount('Bayastan', 10000, 'som', [], True)

ba_bayas.display_balance()
ba_bayas.add_to_balance(5000)
ba_bayas.display_history()
ba_bayas.display_balance()
ba_bayas.withdraw(500)
ba_bayas.display_history()
ba_bayas.display_balance()
