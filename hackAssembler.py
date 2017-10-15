import asmList
import fileHandler

class hackAssembler:
	def __init__(self, filename):
		if filename.find(".asm") == -1:
			print("File type error, .asm file expected.")
			return
		self.filename = filename
		self.filehandler = fileHandler.fileHandler(filename)
		self.asmList = asmList.asmList(self.filehandler.fileContent)
		self.asmList.convert()
		self.filehandler.refreshContent(self.asmList.binCode)
	
	def output(self):
		self.filehandler.appendEnter()
		return self.filehandler.write(self.filename.replace(".asm", ".hack"))
		
	def clear(self):
		self.filehandler.fileContent = []
		self.asmList.asmCode = []
		self.asmList.binCode = []
		self.asmList.count = 0
		self.asmList.labels.list = {}