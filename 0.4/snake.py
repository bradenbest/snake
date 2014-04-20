import time, sys, random

import pygame

pygame.init()

RESOLUTION = (800,800)
WINDOW = pygame.display.set_mode(RESOLUTION,0,32) 
FPS = 1.0 / 60

def rand(n):
  return int(random.random() * n) % n

class Food:
  def __init__(self):
    self.x = 0
    self.y = 0

  def render(self):
    pygame.draw.rect(WINDOW, (255,255,255), (self.x * 10, self.y * 10, 10, 10))

  def run(self):
    self.render()

class SnakePiece:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.active = 0

class Snake:
  def __init__(self):
    self.x = RESOLUTION[0] / 2
    self.y = RESOLUTION[1] / 2
    self.d = rand(4)
    self.pieces = []
    
    for i in range(10):
      self.pieces.append(SnakePiece())
    self.food = Food()

  def move(self):
    if   self.d == 0: 
      self.y -= 1
    elif self.d == 1: 
      self.x += 1
    elif self.d == 2:
      self.y += 1
    elif self.d == 3:
      self.x -= 1

    self.x = self.x % (RESOLUTION[0] / 10)
    self.y = self.y % (RESOLUTION[1] / 10)
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
        pygame.draw.rect(WINDOW, (255,255,255), (p.x * 10, p.y * 10, 10, 10))
      cptr += 1

  def run(self):
    pieces = self.pieces
    self.move()
    self.food.run()
    self.render()

def main():
  s = Snake()
  while 1:
    WINDOW.fill((0,0,0))
    s.run()
    pygame.display.update()
    time.sleep(FPS)

main()
