import time, pygame

pygame.init()
WINDOW = pygame.display.set_mode((800,800),0,32) 

def main():
  x = 0
  while 1:
    WINDOW.fill((0,0,0))
    x += 1
    pygame.draw.rect(WINDOW,(255,255,255),(x,0,100,100))
    pygame.display.update()
    time.sleep(1.0 / 60)

main()
