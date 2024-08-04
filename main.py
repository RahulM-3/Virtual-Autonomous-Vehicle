# imports
import pygame
from math import ceil
from random import randint

# setup
pygame.init()
pygame.display.set_caption("AI Car")
screen = pygame.display.set_mode((800, 600))
running = True
color = (255, 255, 255)

# road sprite
road = pygame.image.load(r"images/Road.png").convert_alpha()
road = pygame.transform.scale(road, (550, 550)) 

# update road
scroll = 0
tiles = ceil(600 / road.get_height()) + 1

# car sprite
mc_car = pygame.image.load(r"images/mc-car.png").convert_alpha()
mc_car = pygame.transform.scale(mc_car, (60, 110))
pos = 200
speed = 0.1

# update every frame
while(running):

    # setup update
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    screen.fill(color)

    # draw road
    i = 0
    while(i < tiles):
        screen.blit(road, (100, road.get_height()*i - scroll)) 
        i += 1
    
    # draw road
    screen.blit(mc_car, (320, pos))

    # update road
    scroll += speed+0.1
    if abs(scroll) > road.get_height():
        scroll = 0

    
    pygame.display.flip()

pygame.quit()