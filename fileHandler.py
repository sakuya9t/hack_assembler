class fileHandler:
	fileContent=[]
	def __init__(self, filename):
		self.filename = filename
		fileObject = open(filename)
		try:
			self.fileContent = fileObject.readlines()
		finally:
			fileObject.close()
	def write(self, filename):
		fileObject = open(filename,'w')
		fileObject.writelines(self.fileContent)
		fileObject.close()
	def refreshContent(self, content):
		self.fileContent = content
	def appendEnter(self):
		length = len(self.fileContent)
		for i in range(0, length - 1):
			self.fileContent[i] += "\n"