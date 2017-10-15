import labelList
class asmList:
	asmCode = []
	binCode = []
	labels = labelList.labelList()
	
	def __init__(self, codeList):
		self.asmCode = codeList
		self.count = -1
		self.initLabel()
		
	def initLabel(self):
		labelid = 16
		for asmLine in self.asmCode:
			asmLine = self.removeComment(asmLine)
			if self.isValid(asmLine):
				self.count += 1
				if self.isJumpLabel(asmLine):
					label = asmLine.replace("(", "").replace(")", "")
					self.labels.add(label, self.count)
					self.count -= 1
		for asmLine in self.asmCode:
			asmLine = self.removeComment(asmLine)
			if self.isACode(asmLine):
				variant = asmLine.replace("@", "")
				if not variant.isdigit() and not self.labels.exists(variant):
					self.labels.add(variant, labelid)
					labelid += 1
		
	def convert(self):
		for asmLine in self.asmCode:
			asmLine = self.removeComment(asmLine)
			if self.isValid(asmLine):
				if self.isACode(asmLine):
					self.binCode.append(self.convertACode(asmLine))
				elif self.isJumpLabel(asmLine):
					continue
				else:
					self.binCode.append(self.convertCCode(asmLine))
		
	def isACode(self, code):
		if len(code) == 0:
			return False
		return code[0] == '@'
		
	def convertACode(self, code):
		dest = code.replace('@', '')
		if not dest.isdigit():
			dest = self.labels.get(dest)
		dest = (int)(dest)
		bindest = bin(dest).split('b')[1]
		cmdlength = len(bindest)
		for i in range(cmdlength, 16):
			bindest = "0" + bindest
		return bindest
		
	def convertCCode(self, code):
		codelist = self.divideCCode(code)
		dest = self.convertDest(codelist[0])
		comp = self.convertComp(codelist[1])
		jump = self.convertJump(codelist[2])
		return "111" + comp + dest + jump
		
	def divideCCode(self, code):
		dest = ""
		comp = ""
		jump = ""
		if code.find("=") > -1:
			dest = code.split("=")[0]
			code = code.split("=")[1]
		if code.find(";") > -1:
			jump = code.split(";")[1]
			code = code.split(";")[0]
		comp = code
		return [dest, comp, jump]
		
	def convertDest(self, dest):
		bincode = ""
		if dest.find("A") > -1:
			bincode += "1"
		else:
			bincode += "0"
		if dest.find("D") > -1:
			bincode += "1"
		else:
			bincode += "0"
		if dest.find("M") > -1:
			bincode += "1"
		else:
			bincode += "0"
		return bincode
		
	def convertComp(self, comp):
		a = "0"
		if comp.find("M") > -1:
			a = "1"
		if comp == "0":
			return a + "101010"
		if comp == "1":
			return a + "111111"
		if comp == "-1":
			return a + "111010"
		if comp == "D":
			return a + "001100"
		if comp == "A" or comp == "M":
			return a + "110000"
		if comp == "!D":
			return a + "001101"
		if comp == "!A" or comp == "!M":
			return a + "110001"
		if comp == "-D":
			return a + "001111"
		if comp == "-A" or comp == "-M":
			return a + "110011"
		if comp == "D+1":
			return a + "011111"
		if comp == "A+1" or comp == "M+1":
			return a + "110111"
		if comp == "D-1":
			return a + "001110"
		if comp == "A-1" or comp == "M-1":
			return a + "110010"
		if comp == "D+A" or comp == "D+M" or comp == "M+D" or comp == "A+D":
			return a + "000010"
		if comp == "D-A" or comp == "D-M":
			return a + "010011"
		if comp == "A-D" or comp == "M-D":
			return a + "000111"
		if comp.find("&") > -1:
			return a + "000000"
		if comp.find("|") > -1:
			return a + "010101"
		return "0101010"
	
	def convertJump(self, jump):
		if jump == "JGT":
			return "001"
		if jump == "JEQ":
			return "010"
		if jump == "JGE":
			return "011"
		if jump == "JLT":
			return "100"
		if jump == "JNE":
			return "101"
		if jump == "JLE":
			return "110"
		if jump == "JMP":
			return "111"
		return "000"
		
	def removeComment(self, code):
		code = code.split("//")[0]
		code = code.replace(' ', '')
		code = code.replace("\n", "")
		return code
		
	def isValid(self, code):
		if code[0:2] == "//":
			return False
		if len(code) == 0:
			return False
		if code == "\n":
			return False
		return True
		
	def isJumpLabel(self, code):
		if code[0] == "(":
			return True
		return False

	def printBinaryCode(self):
		for line in self.binCode:
			print(line)