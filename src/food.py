if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

from functions import *
from constants import *

class Boom: 
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.cap = 20
    self.state = 0
    self.colors = (
      (200,  0,  0),
      (200,200,  0),
      (  0,200,  0),
      (  0,200,200),
      (  0,  0,200),
      (200,  0,200)
    )

  def render(self, rng, s_mod, parent):
    if parent.state >= rng[0] and parent.state <= rng[1]:
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * SCALE, (parent.y-s_mod[0]) * SCALE, s_mod[1] * SCALE, SCALE)) # Top
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * SCALE, (parent.y+s_mod[0]) * SCALE, s_mod[1] * SCALE, SCALE)) # Bottom
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * SCALE, (parent.y-s_mod[0]) * SCALE, SCALE, s_mod[1] * SCALE)) # Left
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x+s_mod[0]) * SCALE, (parent.y-s_mod[0]) * SCALE, SCALE, s_mod[1] * SCALE)) # Right
    

  def run(self, parent):
    if self.state > 0:
      for i in range(1,self.cap):
        self.render((i,i+2), (i,1+(i*2)), self)
      self.state += 1
      if self.state > self.cap:
        parent.boom_ptr += 1

class Food:
  def __init__(self):
    self.x = 0
    self.y = 0
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

