from lab_python_oop.Rectangle import Rectangle


class Square(Rectangle):
	def __init__(self, s, w):
		self.len = w
		super().__init__(s,w,w)
		self.name = 'Square'
	def getname(self):
		return self.name
	def area(self):
		return self.len * self.len
	def __repr__(self):
		return "type: "+ str(self.getname()) +"  length = " + str(self.len) + " area = " + str(self.area()) +" color: " + str(self.color)