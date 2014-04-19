if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

from sys import exit
from time import sleep

from food import Food
from functions import *
from constants import *
from boom import Boom

class SnakePiece:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.active = 0

class Snake:
  def __init__(self):
    self.score = 0
    self.background_color = (0x33,0x33,0x33)
    self.x = (RESOLUTION[0] / SCALE) / 2
    self.y = (RESOLUTION[1] / SCALE) / 2
    self.d = rand(4)
    self.pieces = []
    self.colors = []
    pygame.mixer.music.load("sound/music.wav")
    
    for i in range(10):
      self.pieces.append(SnakePiece())
      self.colors.append(random_color())
    self.foods = [Food() for i in range(5)]

  def music(self):
    if not pygame.mixer.music.get_busy():
      pygame.mixer.music.rewind()
      pygame.mixer.music.play()

  def controls(self):
    for evt in pygame.event.get():
      if evt.type == pygame.KEYDOWN or evt.type == 2:
        key = evt.key
        if   key == pygame.K_UP and self.d != 2 and self.pieces[1].y != self.pieces[0].y - 1:    # Key is up,    direction is not down,  and the piece immediately after the head isn't directly above
          self.d = 0
        elif key == pygame.K_RIGHT and self.d != 3 and self.pieces[1].x != self.pieces[0].x + 1: # Key is right, direction is not left,  and the piece immediately after the head isn't directly to the right
          self.d = 1
        elif key == pygame.K_DOWN and self.d != 0 and self.pieces[1].y != self.pieces[0].y + 1:  # Key is down,  direction is not up,    and the piece immediately after the head isn't directly below
          self.d = 2
        elif key == pygame.K_LEFT and self.d != 1 and self.pieces[1].x != self.pieces[0].x - 1:  # Key is left,  direction is not right, and the piece immediately after the head isn't directly to the left
          self.d = 3

  def move(self):
    if   self.d == 0: 
      self.y -= 1
    elif self.d == 1: 
      self.x += 1
    elif self.d == 2:
      self.y += 1
    elif self.d == 3:
      self.x -= 1

    self.x = self.x % (RESOLUTION[0] / SCALE)
    self.y = self.y % (RESOLUTION[1] / SCALE)
    tail = self.pieces.pop()
    tail.x = self.x
    tail.y = self.y
    tail.active = 1
    self.pieces.reverse()
    self.pieces.append(tail)
    self.pieces.reverse()

  def render(self):
    cptr = 0
    for p in self.pieces:
      if p.active:
        pygame.draw.rect(WINDOW, self.colors[cptr], (p.x * SCALE, p.y * SCALE, SCALE-PADDING, SCALE-PADDING))
      cptr += 1

  def grow(self):
    for i in range(5):
      self.pieces.append(SnakePiece())
      self.colors.append(random_color())
    self.background_color = (rand(0x44),rand(0x44),rand(0x44)) # dark background
    self.score += 100

  def run(self, signal):
    self.music()
    self.controls()
    pieces = self.pieces
    for i in range(len(pieces)):
      if i != 0:
        if collision(pieces[0], pieces[i]) and pieces[0].active and pieces[i].active:
          self.death(signal)
    self.move()
    for food in self.foods:
      food.run(self)
    self.render()

  def death(self, signal): # Snake death animation
    cptr = 0
    pygame.mixer.music.stop()
    pygame.mixer.Sound("sound/death.wav").play()
    # background goes black
    WINDOW.fill((0,0,0))
    self.render()
    pygame.display.update()
    # dramatic pause
    sleep(1.5)
    # each piece disappears
    clock = pygame.time.Clock()
    i = len(self.pieces)
    while i: # Yep, we're going through in reverse
      i -= 1
      p = self.pieces[i]
      p.active = 0
      WINDOW.fill((0,0,0))
      self.render()
      pygame.display.update()
      pygame.mixer.Sound("sound/noise_short_2.wav").play()
      clock.tick(i * 2)
      cptr += 1
    sleep(0.4)
    # BOOM!
    boom = Boom(self.pieces[0].x, self.pieces[0].y)
    boom.cap = 100
    for i in range(boom.cap):
      WINDOW.fill((0,0,0))
      boom.run()
      pygame.display.update()
      sleep((1.0/FPS) / 2)
    # Clear screen
    WINDOW.fill((0,0,0))
    pygame.display.update()
      
    # game over
    #print("Game Over\nScore: %i" % self.score)
    font = pygame.font.Font(None,80)
    font2 = pygame.font.Font(None,60)
    font3 = pygame.font.Font(None,40)
    txt = (
      font.render("G A M E   O V E R",1,(255,255,255)),
      font2.render("Score: %i" % self.score, 1, (255,255,255)),
      font3.render("Press 'q' to quit", 1, (0xaa, 0xaa, 0xaa)),
      font3.render("Press 'r' to restart", 1, (0xaa, 0xaa, 0xaa))
    )
    WINDOW.blit(txt[0],(RESOLUTION[0]/2 - font.size("G A M E   O V E R")[0]/2,RESOLUTION[1]/8))
    WINDOW.blit(txt[1],(RESOLUTION[0]/2 - font2.size("Score: %i" % self.score)[0]/2,(RESOLUTION[1]/8) * 2))
    WINDOW.blit(txt[2],(RESOLUTION[0]/2 - font3.size("Press 'q' to quit")[0]/2,(RESOLUTION[1]/16) * 15))
    WINDOW.blit(txt[3],(RESOLUTION[0]/2 - font3.size("Press 'r' to restart")[0]/2,(RESOLUTION[1]/16) * 14))
    pygame.display.update()
    signal[0] = SIG_NOOP
    while 1:
      for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
          if e.key == pygame.K_q:
            signal[0] = SIG_QUIT
          elif e.key == pygame.K_r:
            signal[0] = SIG_RESTART
      if signal[0]:
        break
