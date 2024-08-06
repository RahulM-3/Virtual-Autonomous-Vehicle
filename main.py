# imports
import pygame
from math import ceil
from car import car
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

# main car sprite
mc_car = car(r"images/mc-car.png", 0.15, 320, 200)
mc_car.resize(60, 110)

# npc car sprite
npc1 = car(r"images/car1.png", 0.05, 325, randint(600, 1000), 378, randint(0, 1))
npc1.resize(50, 100)

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
    
    print(npc1.y)
    print(npc1.lane)

    # draw car
    mc_car.draw(screen)
    npc1.draw(screen)
    npc1.y -= mc_car.speed-npc1.speed

    if(mc_car.collision(npc1) or npc1.y <= 0-100):
        npc1.y = randint(600, 800)
        npc1.lane = randint(0, 1)

    # update road
    scroll += mc_car.speed
    if abs(scroll) > road.get_height():
        scroll = 0


    pygame.display.flip()

pygame.quit()