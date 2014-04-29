import pygame

if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()


DISPLAY_INFO = pygame.display.Info()
RAW_RESOLUTION = (int(DISPLAY_INFO.current_w), int(DISPLAY_INFO.current_h))
SCALE = 10
PADDING = 0
#GRIDSIZE = (60,60)
GRIDSIZE = (int(RAW_RESOLUTION[0] / SCALE), int(RAW_RESOLUTION[1] / SCALE))
RESOLUTION = (int(GRIDSIZE[0] * SCALE), int(GRIDSIZE[1] * SCALE))
WINDOW = pygame.display.set_mode(RESOLUTION,pygame.FULLSCREEN,32) 
FPS = 30

#pygame.display.toggle_fullscreen()

SIG_NOOP = 0
SIG_QUIT = 1
SIG_RESTART = 2

TROLLING_ENABLED = False # Enable this if you dare
