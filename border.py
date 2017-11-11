import pygame
import globalData

class BorderGame(object):
	gameDisplay = pygame.display.set_mode((1080, 720))

	def __init__(self, color, startX, startY, startSize, currImage):
		data.canvasWidth = 1080
		data.canvasHeight = 720
		
		self.currX = -data.canvasWidth
		self.currY = -data.canvasHeight

		self.right = pygame.image.load("images/border/right.png"))
		self.right = pygame.transform.scale(self.right, (40, data.height*3))
		self.left = pygame.image.load("images/border/left.png"))
		self.left = pygame.transform.scale(self.left, (40, data.height*3))
		self.bottom = pygame.image.load("images/border/bottom.png"))
		self.bottom = pygame.transform.scale(self.bottom, (data.width*3, 40))	
		self.top = pygame.image.load("images/border/top.png"))
		self.top = pygame.transform.scale(self.top, (data.width*3, 40))	

	def moveBorder(self, dx, dy):
		currX += dx
		currY += dy
		if not isLegal(): pass

	def drawBorder(self, screen):
		BorderGame.gameDisplay.blit(self.right, (self.currX + data.canvasWidth*3, self.currY))
		BorderGame.gameDisplay.blit(self.left, (self.currX,self.currY))
		BorderGame.gameDisplay.blit(self.bottom, (x,y))
		BorderGame.gameDisplay.blit(self.top, (self.currX, self.currY + data.canvasHeight*3))
		

