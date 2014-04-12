import functions
import constants

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
      constants.pygame.draw.rect(constants.WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * constants.SCALE, (parent.y-s_mod[0]) * constants.SCALE, s_mod[1] * constants.SCALE, constants.SCALE)) # Top
      constants.pygame.draw.rect(constants.WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * constants.SCALE, (parent.y+s_mod[0]) * constants.SCALE, s_mod[1] * constants.SCALE, constants.SCALE)) # Bottom
      constants.pygame.draw.rect(constants.WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * constants.SCALE, (parent.y-s_mod[0]) * constants.SCALE, constants.SCALE, s_mod[1] * constants.SCALE)) # Left
      constants.pygame.draw.rect(constants.WINDOW, parent.colors[rng[0] % 6], ((parent.x+s_mod[0]) * constants.SCALE, (parent.y-s_mod[0]) * constants.SCALE, constants.SCALE, s_mod[1] * constants.SCALE)) # Right
    

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
    self.x = functions.rand(constants.RESOLUTION[0] / constants.SCALE)
    self.y = functions.rand(constants.RESOLUTION[1] / constants.SCALE)
    self.c = functions.random_color()
    self.booms.append(Boom(self.x, self.y))
    self.booms[self.boom_ptr].state = 1
    
  def render(self):
    constants.pygame.draw.rect(constants.WINDOW, self.c, (self.x * constants.SCALE, self.y * constants.SCALE, constants.SCALE-constants.PADDING, constants.SCALE-constants.PADDING))

  def run(self, parent):
    if functions.collision(self,parent):
      parent.grow()
      self.move()
    self.render()
    self.booms[self.boom_ptr].run(self)
