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
    self.x = constants.RESOLUTION[0] / 2
    self.y = constants.RESOLUTION[1] / 2
    self.d = functions.rand(4)
    self.pieces = []
    
    for i in range(10):
      self.pieces.append(SnakePiece())
    self.food = food.Food()

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

  def run(self):
    pieces = self.pieces
    self.move()
    self.food.run()
    self.render()
