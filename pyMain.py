'''
pygamegame.py
created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15
use this code in your term project if you want
- CITE IT
- you can modify it to your liking
  - BUT STILL CITE IT
- you should remove the print calls from any function you aren't using
- you might want to move the pygame.display.flip() to your redrawAll function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''
import globalData
import pygame
import hero
import border

class PygameGame(object):

    def init(self):
        self.width = 1080
        self.height = 720
        self.player = hero.HeroPlayer("b", 1, 0)
        self.border = border.BorderGame()

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.move = 10

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        if x < self.width//2: 
            self.border.moveBorder(self.move,0)
        else: 
            self.border.moveBorder(-self.move,0)
        if y < self.height//2: 
            self.border.moveBorder(0,self.move)
        else: 
            self.border.moveBorder(0,-self.move)

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_LEFT: self.left = True
        if keyCode == pygame.K_RIGHT: self.right = True
        if keyCode == pygame.K_UP: self.up = True
        if keyCode == pygame.K_DOWN: self.down = True

    def keyReleased(self, keyCode, modifier):
        if keyCode == pygame.K_LEFT: self.left = False
        if keyCode == pygame.K_RIGHT: self.right = False
        if keyCode == pygame.K_UP: self.up = False
        if keyCode == pygame.K_DOWN: self.down = False

    def timerFired(self, dt):
        self.player.changeCurrImage()
        if self.left: self.border.moveBorder(self.move,0)
        if self.right: self.border.moveBorder(-self.move,0)
        if self.up: self.border.moveBorder(0,self.move)
        if self.down: self.border.moveBorder(0, -self.move)

    def redrawAll(self, screen):
        self.player.drawHero(screen)
        self.border.drawBorder(screen)

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1080, height=720, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                    
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False

                    
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    class Struct(): pass
    data = Struct()
    data.height = 720
    data.width = 1080
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()

