class HeroPlayer(object):
	def __init__(self, startX, startY, startSize):
		self.currX = startX
		self.currY = startY 
		self.size = startSize

	def moveHero(self, dx, dy):
		currX += dx
		currY += dy
		if not isLegal(): pass

	def isLegal(self): pass

	def drawHero(self, canvas):
		canvas.create_oval(self.currX, self.currY, self.currX + 10, self.currY + 10)

