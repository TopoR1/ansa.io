import pygame

class HeroPlayer(object):
	gameDisplay = pygame.display.set_mode((1080, 720))

	def __init__(self, color, startSize, currImage):
		self.color = color
		self.height = 720
		self.width = 1080
		self.size = startSize
		self.images = self.createImages()
		self.currImage = currImage
		self.pause = 0

	def createImages(self):
		playerImages = []
		for i in range(0,8):
			playerImages.append(pygame.image.load("images/" + self.color + "/" + str(i)+".png"))
		return playerImages

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
		HeroPlayer.gameDisplay.blit(img, (self.width//2, self.height//2))
		#pygame.draw.circle(self.images[self.currImage], (255, 255, 255), (0, 0), 0)


		

