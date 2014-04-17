if __name__ == "__main__":
  print("This is not supposed to be run directly. To run the game, run python with main.py")
  exit()

from random import random

def collision(p1,p2):
  return p1.x == p2.x and p1.y == p2.y

def rand(n):
  return int(random() * n) % n

def random_color():
  return (rand(0xFF),rand(0xFF),rand(0xFF))
