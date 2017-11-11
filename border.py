import pygame
import globalData

class BorderGame(object):
	gameDisplay = pygame.display.set_mode((1080, 720))

	def __init__(self):
		self.width = 1080
		self.height = 720
		
		self.currX = -self.width
		self.currY = -self.height

		self.right = pygame.image.load("images/border/right.png")
		self.right = pygame.transform.scale(self.right, (40, self.height*3))
		self.left = pygame.image.load("images/border/left.png")
		self.left = pygame.transform.scale(self.left, (40, self.height*3))
		self.bottom = pygame.image.load("images/border/bottom.png")
		self.bottom = pygame.transform.scale(self.bottom, (self.width*3, 40))	
		self.top = pygame.image.load("images/border/top.png")
		self.top = pygame.transform.scale(self.top, (self.width*3, 40))	

	def moveBorder(self, dx, dy):
		self.currX += dx
		self.currY += dy
		print(self.currX, self.currY)

	def drawBorder(self, screen):
		BorderGame.gameDisplay.blit(self.right, (self.currX + self.width*3, self.currY))
		BorderGame.gameDisplay.blit(self.left, (self.currX,self.currY))
		BorderGame.gameDisplay.blit(self.bottom, (self.currX, self.currY + self.height*3))
		BorderGame.gameDisplay.blit(self.top, (self.currX, self.currY))
		

