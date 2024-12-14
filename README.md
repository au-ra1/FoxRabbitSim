# FoxRabbitSim
A simulation of foxes and rabbits inspired by the Lotka-Volterra equations

**To use: clone the repository into your IDE or manually download and run the script, python 3.1+ required. Run without debug mode for significantly reduced lag.**

While simplistic, it gives interesting visual effects and some examples of emergent behaviour.

This uses pygame to create a window and clock / time system.

The main logic functions via a 2D array, whereby each coordinate has its own space for an object, like so: environment[i][j][0] environment[i][j][1] environment[i][j][2], grass/rabbit/fox in that order. This enables checks for each tile in the array - e.g. if environment[i][j][0] contains something, then that must be a grass and so any grass functions will be called. The classes themselves will therefore creates objects only in their designated 2D array space.

To move to food e.g. for a rabbit, the function examines a square radius around the object in the array, then checks each side for a grass. The search radius increases to a max of a given value, for each subsequent ring that a grass hasn't been found. Once found, the movement function is simple: e.g. the x axis: if the grass x is > than the rabbit x, then the rabbit x is reduced by -1. This is repeated for each loop until the coordinates of both objects are matching.

The reproduction function mitosis() works by creating a new object in a random location near to the original object. If it is at an edge of the window, it will attempt to place an object within allowable range and repeat if it is not allowed i.e. outside the window, for a set amount of loops (10). To better control likelihood of reproduction occuring, an array from 0-10 is used, where a random number is chosen and if this number is >= x, then it will reproduce. 

One potential downside to this is that if two of the same object enter the same location, then one of them is deleted. This isn't a problem in terms of displaying the final result, but ultimately does result in less accurate portrayal of how many rabbits or foxes actually exist in a given timeframe.

Manually changing parameters such as create_grass(x) in the main loop, the range(x) of the find_grass or find_rabbit functions, or chance_mitosis <=x all result in interesting different patterns.
