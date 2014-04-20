import time   # for FPS

import constants
import snake

def main():
  s = snake.Snake()
  while 1:
    constants.WINDOW.fill((0,0,0))
    s.run()
    constants.pygame.display.update()
    time.sleep(constants.FPS)

main()
