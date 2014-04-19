# Standard Library
from sys import exit

# Dependencies / Local imports (import organization; learned it from C)
from constants import *
from snake import Snake

def main():
  s = Snake()
  clock = pygame.time.Clock()
  signal = [SIG_NOOP] # it's an array to make sure Snake.run() actually modifies THIS, instead of making a copy and discarding it when it goes out of scope
  while 1:
    WINDOW.fill(s.background_color)
    s.run(signal)
    if signal[0]: break
    pygame.display.update()
    clock.tick(FPS)
  if signal[0] == SIG_QUIT:
    pygame.quit()
    exit()
  elif signal[0] == SIG_RESTART:
    main()

if __name__ == "__main__":
  main()
else:
  print("I dunno why you're trying to run this as a module, but stop it. Stop it before you tear the very fabric of the universe itself!")
  pygame.quit()
  exit()
