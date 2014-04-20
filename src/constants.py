import pygame

if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

RESOLUTION = (800,800)
WINDOW = pygame.display.set_mode(RESOLUTION,0,32) 
FPS = 30
SCALE = 10
PADDING = 0

SIG_NOOP = 0
SIG_QUIT = 1
SIG_RESTART = 2
