import pygame
import globalData

class BorderGame(object):
	gameDisplay = pygame.display.set_mode((data.width, data.height))

	def __init__(self, color, startX, startY, startSize, currImage):
		
		self.currX = startX
		self.currY = startY 
		self.size = startSize

		self.right = pygame.image.load("images/border/right.png"))
		self.left = pygame.image.load("images/border/left.png"))
		self.bottom = pygame.image.load("images/border/bottom.png"))	
		self.top = pygame.image.load("images/border/top.png"))

	def moveBorder(self, dx, dy):
		currX += dx
		currY += dy
		if not isLegal(): pass



"""

	def changeCurrImage(self):
		if self.currImage < 7 and self.pause == 4:
			self.currImage += 1
			self.pause = 0
		if self.currImage == 7:
			self.currImage = 0
		self.pause += 1

	def isLegal(self): pass

	def drawHero(self, screen):
		img = pygame.transform.scale(self.images[self.currImage], (50,50))
		HeroPlayer.gameDisplay.blit(img, (self.currX, self.currY))"""

		

