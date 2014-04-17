if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

from sys import exit

from food import Food
from functions import *
from constants import *

class SnakePiece:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.active = 0

class Snake:
  def __init__(self):
    self.score = 0
    self.background_color = (0,0,0)
    self.x = (RESOLUTION[0] / SCALE) / 2
    self.y = (RESOLUTION[1] / SCALE) / 2
    self.d = rand(4)
    self.pieces = []
    self.colors = []
    
    for i in range(10):
      self.pieces.append(SnakePiece())
      self.colors.append(random_color())
    self.food = Food()

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

  def run(self):
    self.controls()
    pieces = self.pieces
    for i in range(len(pieces)):
      if i != 0:
        if collision(pieces[0], pieces[i]) and pieces[0].active and pieces[i].active:
          print("Game Over\nScore: %i" % self.score)
          pygame.quit()
          exit()
    self.move()
    self.food.run(self)
    self.render()
