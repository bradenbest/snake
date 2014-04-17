if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

from functions import *
from constants import *
from boom import Boom

class Food:
  def __init__(self):
    self.x = rand(RESOLUTION[0] / SCALE)
    self.y = rand(RESOLUTION[1] / SCALE)
    self.c = (0xff, 0xff, 0xff)
    self.booms = []
    self.boom_ptr = 0
    self.booms.append(Boom(self.x, self.y))

  def move(self):
    self.x = rand(RESOLUTION[0] / SCALE)
    self.y = rand(RESOLUTION[1] / SCALE)
    self.c = random_color()
    self.booms.append(Boom(self.x, self.y))
    self.booms[self.boom_ptr].state = 1
    
  def render(self):
    pygame.draw.rect(WINDOW, self.c, (self.x * SCALE, self.y * SCALE, SCALE-PADDING, SCALE-PADDING))

  def run(self, parent):
    if collision(self,parent):
      parent.grow()
      self.move()
    self.render()
    self.booms[self.boom_ptr].run(self)

