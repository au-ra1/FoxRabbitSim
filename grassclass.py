from config import *
class grass(): #creates grass at random coordinates
    def __init__(self):
        self.x = random.randint(0, WIN_WIDTH -1)
        self.y = random.randint(0, WIN_HEIGHT -1) 
    def display(self):
         screen.set_at((self.x, self.y), green)
class test_grass(): #creates grass at specific coordinates
  def __init__(self, x, y):
      self.x = x
      self.y = y
  def display(self):
      screen.set_at((self.x, self.y), green)           