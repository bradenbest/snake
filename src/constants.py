import pygame

if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

GRIDSIZE = (60,60)
SCALE = 10
PADDING = 0
RESOLUTION = (GRIDSIZE[0] * SCALE, GRIDSIZE[1] * SCALE)
WINDOW = pygame.display.set_mode(RESOLUTION,0,32) 
FPS = 30

SIG_NOOP = 0
SIG_QUIT = 1
SIG_RESTART = 2

TROLLING_ENABLED = False # Enable this if you dare
