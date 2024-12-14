#this file contains all the functions called outside of the main loop
from config import *
from rabbitclass import *
from grassclass import *
from foxclass import*

def reset_display(): #resets the display
    for x in range(WIN_WIDTH):
        for y in range(WIN_HEIGHT):
            screen.set_at((x, y), black)     
            
def create_grass(): #creates grass object
     mygrass = grass()
     environment[mygrass.x][mygrass.y][0] = mygrass
     
def create_test_grass(x, y): #creates a specific grass at desired coordinates for testing
     mygrass = test_grass(x, y)
     environment[mygrass.x][mygrass.y][0] = mygrass
     
def create_rabbit(x, y): #creates rabbit object
     myrabbit = initial_rabbit(x, y)
     environment[myrabbit.x][myrabbit.y][1] = myrabbit 
     
def create_fox(x, y): #creates fox object
     myfox = initial_fox(x, y)
     environment[myfox.x][myfox.y][2] = myfox 