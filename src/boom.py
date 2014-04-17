if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

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
    self.boom_snd = pygame.mixer.Sound("sound/boom.wav")

  def render(self, rng, s_mod, parent):
    if parent.state >= rng[0] and parent.state <= rng[1]:
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * SCALE, (parent.y-s_mod[0]) * SCALE, s_mod[1] * SCALE, SCALE)) # Top
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * SCALE, (parent.y+s_mod[0]) * SCALE, s_mod[1] * SCALE, SCALE)) # Bottom
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x-s_mod[0]) * SCALE, (parent.y-s_mod[0]) * SCALE, SCALE, s_mod[1] * SCALE)) # Left
      pygame.draw.rect(WINDOW, parent.colors[rng[0] % 6], ((parent.x+s_mod[0]) * SCALE, (parent.y-s_mod[0]) * SCALE, SCALE, s_mod[1] * SCALE)) # Right
    

  def run(self, parent):
    if self.state > 0:
      if self.state == 1:
        self.boom_snd.play()
      for i in range(1,self.cap):
        self.render((i,i+2), (i,1+(i*2)), self)
      self.state += 1
      if self.state > self.cap and hasattr(parent, 'boom_ptr'):
        parent.boom_ptr += 1
