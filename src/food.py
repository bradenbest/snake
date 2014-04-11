import functions
import constants

class Food:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.c = (0xff, 0xff, 0xff)

  def move(self):
    self.x = functions.rand(constants.RESOLUTION[0] / constants.SCALE)
    self.y = functions.rand(constants.RESOLUTION[1] / constants.SCALE)
    self.c = functions.random_color()
    
  def render(self):
    constants.pygame.draw.rect(constants.WINDOW, self.c, (self.x * constants.SCALE, self.y * constants.SCALE, constants.SCALE-constants.PADDING, constants.SCALE-constants.PADDING))

  def run(self, parent):
    if functions.collision(self,parent):
      parent.grow()
      self.move()
    self.render()
