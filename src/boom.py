if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

from constants import *

class Boom: 
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.cap = 20
    self.state = 1
    self.colors = (
      (200,  0,  0),
      (200,200,  0),
      (  0,200,  0),
      (  0,200,200),
      (  0,  0,200),
      (200,  0,200)
    )
    self.boom_snd = pygame.mixer.Sound("sound/boom.wav")

  def render(self, rng, s_mod, cam): 
    # rng = range, it is how many rings of the explosion are visible at one time
    # s_mod = size modifier. it determines the visual progress of the blast
    if self.state >= rng[0] and self.state <= rng[1]:
      pygame.draw.rect(WINDOW, self.colors[rng[0] % 6], ((self.x-s_mod[0]) * SCALE - cam.x, (self.y-s_mod[0]) * SCALE - cam.y, s_mod[1] * SCALE, SCALE)) # Top
      pygame.draw.rect(WINDOW, self.colors[rng[0] % 6], ((self.x-s_mod[0]) * SCALE - cam.x, (self.y+s_mod[0]) * SCALE - cam.y, s_mod[1] * SCALE, SCALE)) # Bottom
      pygame.draw.rect(WINDOW, self.colors[rng[0] % 6], ((self.x-s_mod[0]) * SCALE - cam.x, (self.y-s_mod[0]) * SCALE - cam.y, SCALE, s_mod[1] * SCALE)) # Left
      pygame.draw.rect(WINDOW, self.colors[rng[0] % 6], ((self.x+s_mod[0]) * SCALE - cam.x, (self.y-s_mod[0]) * SCALE - cam.y, SCALE, s_mod[1] * SCALE)) # Right
    

  def run(self, cam):
    if self.state > 0:
      cam.shake()
      if self.state == 1:
        self.boom_snd.play()
      for i in range(1,self.cap):
        self.render((i,i+2), (i,1+(i*2)), cam)
      self.state += 1
      if self.state > self.cap:
        self.state = 0
