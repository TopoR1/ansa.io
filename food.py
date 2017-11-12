import random
import pygame

class Food(object):
    gameDisplay = pygame.display.set_mode((1080, 720))

    def __init__(self):
        minSize = 10
        maxSize = 50
        self.size = random.randint(minSize, maxSize)

        self.width = 1080
        self.height = 720

        screenLeft = -self.width/2
        screenRight = self.width*1.5
        screenTop = -self.height/2
        screenBottom = self.height*1.5
        
        self.x = random.randint(screenLeft, screenRight)
        self.y = random.randint(screenTop, screenBottom)
        
    def __repr__(self):
        return "mass = %d, x = %d, y = %d" %(self.size, self.x, self.y)
    
    def getMassUnits(self):
        return self.size
        
    def getPos(self):
        return (self.x, self.y)
    
    #Collision calls this function
    def collide(self):
        data.foodList.remove((self.size, self.x, self.y))
    
    #Draw is called from canvas
    def drawFood(self, screen, foodImgs):
        randIndex = random.randint(0, 14)
        #foodImgs is passed in as a list of paths to the images
        img = pygame.transform.scale(foodImgs[randIndex], (self.size, self.size))
        #Can we use pygame blit here?
        Food.gameDisplay.blit(img, (self.x, self.y))
