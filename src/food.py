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

  def move(self):
    self.x = rand(RESOLUTION[0] / SCALE)
    self.y = rand(RESOLUTION[1] / SCALE)
    self.c = random_color()
    
  def render(self):
    pygame.draw.rect(WINDOW, self.c, (self.x * SCALE, self.y * SCALE, SCALE-PADDING, SCALE-PADDING))

  def run(self, parent):
    if collision(self,parent):
      parent.grow()
      self.booms.append(Boom(self.x, self.y))
      self.move()
    self.render()
    for b in self.booms:
      b.run()

