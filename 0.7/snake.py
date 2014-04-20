import sys

import food
import functions
import constants

class SnakePiece:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.active = 0

class Snake:
  def __init__(self):
    self.score = 0
    self.x = constants.RESOLUTION[0] / 2
    self.y = constants.RESOLUTION[1] / 2
    self.d = functions.rand(4)
    self.pieces = []
    
    for i in range(10):
      self.pieces.append(SnakePiece())
    self.food = food.Food()

  def controls(self):
    for evt in constants.pygame.event.get():
      if evt.type == constants.pygame.KEYDOWN or evt.type == 2:
        key = evt.key
        if   key == constants.pygame.K_UP and self.d != 2:
          self.d = 0
        elif key == constants.pygame.K_RIGHT and self.d != 3:
          self.d = 1
        elif key == constants.pygame.K_DOWN and self.d != 0:
          self.d = 2
        elif key == constants.pygame.K_LEFT and self.d != 1:
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

    self.x = self.x % (constants.RESOLUTION[0] / constants.SCALE)
    self.y = self.y % (constants.RESOLUTION[1] / constants.SCALE)
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
        constants.pygame.draw.rect(constants.WINDOW, (255,255,255), (p.x * constants.SCALE, p.y * constants.SCALE, constants.SCALE-constants.PADDING, constants.SCALE-constants.PADDING))
      cptr += 1

  def grow(self):
    for i in range(5):
      self.pieces.append(SnakePiece())
    self.score += 100

  def run(self):
    self.controls()
    pieces = self.pieces
    for i in range(len(pieces)):
      if i != 0:
        if functions.collision(pieces[0], pieces[i]) and pieces[0].active and pieces[i].active:
          print("Game Over\nScore: %i" % self.score)
          constants.pygame.quit()
          sys.exit()
    self.move()
    self.food.run(self)
    self.render()
