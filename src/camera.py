class Camera:
  x = 0
  y = 0
  state = 0
  positions = ( # This is the dramatic 'screen shake' animation of the camera
    (8,-4), # right, up (instense)
    (0,0),  # neutral
    (-6,3), # left, down (rough)
    (0,0),  # neutral
    (-4,-2),# left, up (less intense)
    (0,0),  # neutral
    (2,1),  # right, down (calming down)
    (0,0),  # neutral
    (2,-1), # right, up
    (-2,1), # left, down
    (0,0),  # neutral
    (-2,-1),# left, up
    (2,1),  # right, down
    (0,0),  # and 4 frames of neutral
    (0,0),
    (0,0),
    (0,0)
  )

  def shake(self):
    self.x = self.positions[self.state][0]
    self.y = self.positions[self.state][1]
    self.state += 1
    self.state = self.state % len(self.positions)

