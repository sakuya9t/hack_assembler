class labelList:
	list={}
	def __init__(self):
		self.add("SP", 0)
		self.add("LCL", 1)
		self.add("ARG", 2)
		self.add("THIS", 3)
		self.add("THAT", 4)
		self.add("R0", 0)
		self.add("R1", 1)
		self.add("R2", 2)
		self.add("R3", 3)
		self.add("R4", 4)
		self.add("R5", 5)
		self.add("R6", 6)
		self.add("R7", 7)
		self.add("R8", 8)
		self.add("R9", 9)
		self.add("R10", 10)
		self.add("R11", 11)
		self.add("R12", 12)
		self.add("R13", 13)
		self.add("R14", 14)
		self.add("R15", 15)
		self.add("SCREEN", 16384)
		self.add("KBD", 24576)
		
	def add(self, label, value):
		self.list[label] = value
	def get(self, label):
		if label in self.list:
			return self.list[label]
		else:
			return
	def exists(self, label):
		return label in self.list;
