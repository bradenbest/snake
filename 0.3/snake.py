import time, sys, random, pygame

pygame.init()
WINDOW = pygame.display.set_mode((800,800),0,32) 

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

class Snake:
  def __init__(self):
    self.x = 800 / 2
    self.y = 800 / 2
    self.d = rand(4)
    self.pieces = []
    
    for i in range(10):
      self.pieces.append(SnakePiece())
    self.food = Food()

  def move(self):
    if   self.d == 0: self.y -= 1
    elif self.d == 1: self.x += 1
    elif self.d == 2: self.y += 1
    elif self.d == 3: self.x -= 1

    self.x = self.x % (800 / 10)
    self.y = self.y % (800 / 10)
    tail = self.pieces.pop()
    tail.x = self.x
    tail.y = self.y
    self.pieces.reverse()
    self.pieces.append(tail)
    self.pieces.reverse()

  def render(self):
    for p in self.pieces:
      pygame.draw.rect(WINDOW, (255,255,255), (p.x * 10, p.y * 10, 10, 10))

  def run(self):
    self.move()
    self.food.run()
    self.render()

def main():
  s = Snake()
  while 1:
    WINDOW.fill((0,0,0))
    s.run()
    pygame.display.update()
    time.sleep(1.0 / 60)

main()
