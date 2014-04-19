# Standard Library
from sys import exit

# Dependencies / Local imports (import organization; learned it from C)
from constants import *
from snake import Snake

def main():
  s = Snake()
  clock = pygame.time.Clock()
  while 1:
    WINDOW.fill(s.background_color)
    s.run()
    pygame.display.update()
    clock.tick(FPS)

if __name__ == "__main__":
  main()
else:
  print("I dunno why you're trying to run this as a module, but stop it. Stop it before you tear the very fabric of spacetime itself!")
  pygame.quit()
  exit()
