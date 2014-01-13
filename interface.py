class Interface(object):
	def __init__(self):
		self.test = 5

	def read(self):
		return raw_input(">>> ")

	def write(self, msg):
		print msg