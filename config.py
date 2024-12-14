#this file contains our global variables - size of window, colours, and size of the 2D array 
import random
import pygame
import sys

WIN_WIDTH = 250
WIN_HEIGHT = 250
black = (0,0,0)
white = (200,200,200)
green = (0,255,0)
red = (255,0,0)
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))   
environment = [[[None, None, None]for _ in range(WIN_HEIGHT)] for _ in range(WIN_WIDTH)]

