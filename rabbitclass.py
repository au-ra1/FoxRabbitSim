#same as fox mostly, check foxclass.py for documentation
from config import *
class rabbit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 5
        self.grass_array = []
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def position(self):
         return (self.x, self.y)
    def display(self):
          screen.set_at((self.x, self.y), white)
    def age_growth(self):   
         if self.age > 20:
             environment[self.x][self.y][1] = None
         else: 
             self.age +=1                   
    def find_grass(self):  
        grass_exists = False
        for r in range(7):
          for s in range(max(self.x - r, 0), min(self.x +r +1,WIN_WIDTH -1)): 
             top_y = max(self.y -r, 0)
             bottom_y = min(self.y + r, WIN_HEIGHT - 1)
             if environment[s][top_y][0] != None:
              self.grass_array.append((s,top_y))
              grass_exists = True
             if environment[s][bottom_y][0] != None:
              self.grass_array.append((s, bottom_y))
              grass_exists = True   
          for s in range(max(self.y - r + 1, 0), min(self.y +r, WIN_HEIGHT -1)):
             left_x = max(self.x -r, 0)
             right_x = min(self.x +r, WIN_WIDTH -1)   
             if environment[left_x][s][0] != None:
              self.grass_array.append((left_x, s))
              grass_exists = True
             if environment[right_x][s][0] != None:
              self.grass_array.append((right_x, s))
              grass_exists = True        
          if grass_exists == True:
           break         
    def move(self): 
        if self.grass_array == []:
         self.x += random.randint(-1, 1)
         self.x = min(self.x, WIN_WIDTH -1)
         self.x = max(self.x, 0)
         self.y += random.randint(-1, +1)
         self.y = min(self.y, WIN_HEIGHT -1)
         self.y = max(self.y, 0)
        else:
         self.grass_index = random.randint(0, len(self.grass_array)-1)
         self.grass_coord = self.grass_array[self.grass_index]
         if self.grass_coord[0] > self.x:
             self.x += 1
         elif self.grass_coord[0] < self.x:
             self.x -= 1
         if self.grass_coord[1] > self.y:
             self.y += 1
         elif self.grass_coord[1] < self.y:
             self.y -= 1   
         self.eat()
    def mitosis(self): 
        if self.age == 0:
            chance_array = [0,1,2,3,4,5,6,7,8,9,10]
            chance_mitosis = random.choice(chance_array)
            if chance_mitosis <=8:
                spawn_array = [-5,-4,-3,-2,-1,1,2,3,4,5]
                for i in range(10):
                 spawn_locationx = random.choice(spawn_array)
                 spawn_locationy = random.choice(spawn_array)
                 newx = self.x + spawn_locationx
                 newy = self.y + spawn_locationy
                 if 0 <= newx <= WIN_WIDTH -1 and 0 <= newy <= WIN_HEIGHT -1:
                  environment[newx][newy][1] = rabbit(newx, newy)
                  return
    def  clear_grass_array(self):
          self.grass_array.clear()          
    def eat(self):
      if environment[self.x][self.y][0]:
         environment[self.x][self.y][0] = None
         self.age = 0 

class initial_rabbit(rabbit):  
       def __init__(self, x, y):
        super().__init__(x, y)
       def age_growth(self):   
        if self.age > 200:
            environment[self.x][self.y][1] = None
        else: 
            self.age +=1
