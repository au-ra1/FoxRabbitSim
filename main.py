
from config import *
from functiondefs import *
from rabbitclass import *
from foxclass import *
from grassclass import *



def main():
    pygame.init()
    clock = pygame.time.Clock()
    create_rabbit(125,125) #creates initial rabbit and fox at desired coords
    create_fox(240,240)
    # create_test_grass(130, 130)
    print_counter = 0
    while True: #main loop
        reset_display()
        rabbit_count = 0
        fox_count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()                        

        for i in range(WIN_WIDTH): #Displays the creates grass objects in the 2D array
            for j in range(WIN_HEIGHT): 
                if environment[i][j][0] != None:
                    environment[i][j][0].display() 
                    
        for i in range(200): #designates how much grass is spawning per loop
            create_grass()    
            
        for i in range(WIN_WIDTH): #do rabbit functions
            for j in range(WIN_HEIGHT): 
                if environment[i][j][1] != None: 
                    rabbit_count += 1
                    environment[i][j][1].find_grass()
                    environment[i][j][1].move()
                    environment[i][j][1].clear_grass_array()
                    environment[i][j][1].mitosis() 
                    environment[i][j][1].display() 
                    environment[i][j][1].age_growth()
            
        for i in range(WIN_WIDTH): #do fox functions
            for j in range(WIN_HEIGHT): 
                if environment[i][j][2] != None: 
                    fox_count += 1
                    environment[i][j][2].find_rabbit()
                    environment[i][j][2].move()
                    environment[i][j][2].move()
                    environment[i][j][2].clear_rabbit_array()
                    environment[i][j][2].mitosis() 
                    environment[i][j][2].display() 
                    environment[i][j][2].age_growth() 

            
        for i in range(WIN_WIDTH): #rabbit 2D array update positions
            for j in range(WIN_HEIGHT):
                if environment[i][j][1] != None:  
                    rabbitx = environment[i][j][1].get_x()
                    rabbity = environment[i][j][1].get_y()
                    environment[rabbitx][rabbity][1] = environment[i][j][1]
                    if not (rabbitx == i and rabbity == j):
                        environment[i][j][1] = None      
                
        for i in range(WIN_WIDTH): #fox 2D array update positions
            for j in range(WIN_HEIGHT):
                if environment[i][j][2] != None:  
                    foxx = environment[i][j][2].get_x()
                    foxy = environment[i][j][2].get_y()
                    environment[foxx][foxy][2] = environment[i][j][2]
                    if not (foxx == i and foxy == j):
                        environment[i][j][2] = None                  
                          
        pygame.display.update()
        clock.tick()
        print_counter +=1
        if print_counter == 20:
            print_counter = 0
            print("Current number of rabbits (white): " , rabbit_count , " Current number of foxes (red): " , fox_count)
main()




   



            



