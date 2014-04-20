import time, pygame

pygame.init()
WINDOW = pygame.display.set_mode((800,800),0,32) 

class SnakePiece:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Snake:
  def __init__(self):
    self.x = 800 / 2
    self.y = 800 / 2
    self.pieces = []
    
    for i in range(10):
      self.pieces.append(SnakePiece(i,0))

  def run(self):
    for p in self.pieces:
      pygame.draw.rect(WINDOW, (255,255,255), (p.x * 10, p.y * 10, 8, 8))

def main():
  s = Snake()
  while 1:
    WINDOW.fill((0,0,0))
    s.run()
    pygame.display.update()
    time.sleep(1.0 / 60)

main()
