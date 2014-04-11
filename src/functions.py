import random

def collision(p1,p2):
  return p1.x == p2.x and p1.y == p2.y

def rand(n):
  return int(random.random() * n) % n

def random_color():
  return (rand(0xFF),rand(0xFF),rand(0xFF))
