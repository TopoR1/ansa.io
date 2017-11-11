import pygame
import globalData

class BorderGame(object):
	gameDisplay = pygame.display.set_mode((1080, 720))

	def __init__(self):
		self.width = 1080
		self.height = 720
		
		self.currX = -self.width/2
		self.currY = -self.height/2

		self.right = pygame.image.load("images/border/right.png")
		self.right = pygame.transform.scale(self.right, (40, self.height*2))
		self.left = pygame.image.load("images/border/left.png")
		self.left = pygame.transform.scale(self.left, (40, self.height*2))
		self.bottom = pygame.image.load("images/border/bottom.png")
		self.bottom = pygame.transform.scale(self.bottom, (self.width*2, 40))	
		self.top = pygame.image.load("images/border/top.png")
		self.top = pygame.transform.scale(self.top, (self.width*2, 40))	

	def moveBorder(self, dx, dy):
		self.currX += dx
		self.currY += dy
		print(self.currX, self.currY, "Settings", -self.width/2, -self.height/2)
		if not self.isLegal():
			self.currX -= dx
			self.currY -= dy

	def isLegal(self):
		if -1*self.currX < -self.width/2 or -1*self.currX > self.width*1.5: return False
		if -1*self.currY < -self.height/2 or -1*self.currY > self.height*1.5: return False
		return True

	def drawBorder(self, screen):
		BorderGame.gameDisplay.blit(self.right, (self.currX + self.width*2, self.currY))
		BorderGame.gameDisplay.blit(self.left, (self.currX,self.currY))
		BorderGame.gameDisplay.blit(self.bottom, (self.currX, self.currY + self.height*2))
		BorderGame.gameDisplay.blit(self.top, (self.currX, self.currY))
