import time   # for FPS

import constants
import snake

def main():
  s = snake.Snake()
  while 1:
    constants.WINDOW.fill(s.background_color)
    s.run()
    constants.pygame.display.update()
    time.sleep(constants.FPS)

main()
