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
		if not self.isLegal():
			self.currX -= dx
			self.currY -= dy

	def isLegal(self):
		padding = 29
		if -1*self.currX < -self.width/2 + padding or -1*self.currX > self.width*1.5 - padding: return False
		if -1*self.currY < -self.height/2 + padding or -1*self.currY > self.height*1.5 - padding: return False
		return True

	def drawBorder(self, screen):
		#draw the void
		pygame.draw.rect(screen, (171,171,171), (self.currX - self.width/2, self.currY - self.height/2,self.width/2 + 30,self.height*3), 0)
		pygame.draw.rect(screen, (171,171,171), (self.currX + self.width*2+20, self.currY - self.height/2,self.currX + self.width*2,self.height*3), 0)
		pygame.draw.rect(screen, (171,171,171), (self.currX, self.currY - self.height/2, self.currX + self.width*5, self.height/2 + 30), 0)
		pygame.draw.rect(screen, (171,171,171), (self.currX, self.currY + self.height*2+20, self.currX + self.width*5, self.currY + self.height*2), 0)

		#draw the stones of my soul
		BorderGame.gameDisplay.blit(self.right, (self.currX + self.width*2, self.currY))
		BorderGame.gameDisplay.blit(self.left, (self.currX,self.currY))
		BorderGame.gameDisplay.blit(self.bottom, (self.currX, self.currY + self.height*2))
		BorderGame.gameDisplay.blit(self.top, (self.currX, self.currY))
