import pygame

if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

pygame.init()

RESOLUTION = (800,800)
WINDOW = pygame.display.set_mode(RESOLUTION,0,32) 
FPS = 1.0 / 60
SCALE = 10
PADDING = 0
