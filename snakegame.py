import pygame
from snakegame_functions import run #importing functions from other file
pygame.init()

width = 400 #constants again
height = 400
clock = pygame.time.Clock()
snake_pixel_size = 10
snake_speed = 10

window = pygame.display.set_mode((width,height)) #setting up display and caption again
pygame.display.set_caption('Snake game')

run() #running function