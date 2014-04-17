# Standard Library
from time import sleep
from sys import exit

# Dependencies / Local imports (import organization; learned it from C)
from constants import *
from snake import Snake

def main():
  s = Snake()
  while 1:
    WINDOW.fill(s.background_color)
    s.run()
    pygame.display.update()
    sleep(FPS)

if __name__ == "__main__":
  main()
else:
  print("I dunno why you're trying to run this as a module, but stop it. Stop it before you tear the very fabric of spacetime itself!")
  pygame.quit()
  exit()
