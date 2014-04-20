import functions
import constants

class Food:
  def __init__(self):
    self.x = 0
    self.y = 0

  def render(self):
    constants.pygame.draw.rect(constants.WINDOW, (255,255,255), (self.x * constants.SCALE, self.y * constants.SCALE, constants.SCALE-constants.PADDING, constants.SCALE-constants.PADDING))

  def run(self):
    self.render()
