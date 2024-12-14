from config import *
class fox(): #Our fox class
    def __init__(self, x, y): #self parameters
        self.x = x
        self.y = y
        self.age = 1
        self.rabbit_array = []
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def position(self):
         return (self.x, self.y)
    def display(self):
          screen.set_at((self.x, self.y), red)
    def age_growth(self):   #kills the fox if it reaches a certain age
         if self.age > 20:
             environment[self.x][self.y][2] = None
         else: 
             self.age +=1                   
    def find_rabbit(self):  #algorithm for finding its food. Checks in a square radius around itself, by checking top and bottom then left and right sides of the square; appends it to a food array
        rabbit_exists = False
        for r in range(5):
          for s in range(max(self.x - r, 0), min(self.x +r +1,WIN_WIDTH -1)): #top and bottom edges
             top_y = max(self.y -r, 0)
             bottom_y = min(self.y + r, WIN_HEIGHT - 1)
             if environment[s][top_y][1] != None:
              self.rabbit_array.append((s,top_y))
              rabbit_exists = True
             if environment[s][bottom_y][1] != None:
              self.rabbit_array.append((s, bottom_y))
              rabbit_exists = True   
          for s in range(max(self.y - r + 1, 0), min(self.y +r, WIN_HEIGHT -1)): #left and right edges
             left_x = max(self.x -r, 0)
             right_x = min(self.x +r, WIN_WIDTH -1)   
             if environment[left_x][s][1] != None:
              self.rabbit_array.append((left_x, s))
              rabbit_exists = True
             if environment[right_x][s][1] != None:
              self.rabbit_array.append((right_x, s))
              rabbit_exists = True        
          if rabbit_exists == True: #the closest food that is found will break the loop, preventing it from searching for more and wasting resources.
           break         
    def move(self): #moving to the food algorithm. Checks the internal food array, and moves the x/y coordinates of the fox/rabbit to that location one pixel at a time. If none is found, moves randomly
        if self.rabbit_array == []:
         self.x += random.randint(-1, 1)
         self.x = min(self.x, WIN_WIDTH -1)
         self.x = max(self.x, 0)
         self.y += random.randint(-1, +1)
         self.y = min(self.y, WIN_HEIGHT -1)
         self.y = max(self.y, 0)
        else:
         self.rabbit_index = random.randint(0, len(self.rabbit_array)-1)
         self.rabbit_coord = self.rabbit_array[self.rabbit_index]
         if self.rabbit_coord[0] > self.x:
             self.x += 1
         elif self.rabbit_coord[0] < self.x:
             self.x -= 1
         if self.rabbit_coord[1] > self.y:
             self.y += 1
         elif self.rabbit_coord[1] < self.y:
             self.y -= 1   
         self.eat()
    def mitosis(self): #reproduction function. Will add a new class object near the original if the age == 0 (which happens after finding food)
        if self.age == 0:
            chance_array = [0,1,2,3,4,5,6,7,8,9,10]
            chance_mitosis = random.choice(chance_array)
            if chance_mitosis <=2:
                spawn_array = [-5,-4,-3,-2,-1,1,2,3,4,5]
                for i in range(10):
                 spawn_locationx = random.choice(spawn_array)
                 spawn_locationy = random.choice(spawn_array)
                 newx = self.x + spawn_locationx
                 newy = self.y + spawn_locationy
                 if 0 <= newx <= WIN_WIDTH -1 and 0 <= newy <= WIN_HEIGHT -1:
                  environment[newx][newy][2] = fox(newx, newy)
                  return
    def  clear_rabbit_array(self):
          self.rabbit_array.clear()          
    def eat(self): # deletes grass underneath it and sets age to 0
      if environment[self.x][self.y][1]:
         environment[self.x][self.y][1] = None
         self.age = 0 
         
class initial_fox(fox):  
       def __init__(self, x, y):
        super().__init__(x, y)
       def age_growth(self):   
        if self.age > 500:
            environment[self.x][self.y][1] = None
        else: 
            self.age +=1
