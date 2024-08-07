# imports
import pygame
from math import ceil
from car import car
from random import randint, uniform
from sensor import *

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
mc_car = car(r"images/mc_car.png", 0.15, 320, 200)
mc_car.resize(60, 110)

# npc car sprite
npc1 = car(r"images/car2.png", uniform(0.05, 0.12), 322, randint(600, 1200), 375, randint(0, 1))
npc1.resize(55, 100)
npc2 = car(r"images/car1.png", uniform(0.05, 0.12), 325, randint(600, 1200), 378, randint(0, 1))
npc2.resize(50, 100)

npc_cars = [npc1, npc1, npc2, npc2]

def update(npc_car) -> bool:
    if(mc_car.collision(npc_car) or npc_car.y <= 0-100):
        npc_car.speed = uniform(0.05, 0.12)
        npc_car.y = randint(600, 1200)
        npc_car.lane = randint(0, 1)
        return True
    return False

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
    
    # activare lidar
    car_lidar = lidar(screen, (350, 250))
    # draw car
    mc_car.draw(screen)
    
    for i in range(4):
        car_lidar.get_data(npc_cars[i])
        npc_cars[i].draw(screen)
        npc_cars[i].y -= mc_car.speed-npc_cars[i].speed
        speed = npc_cars[i].speed
        l = npc_cars[i].lane
        if(update(npc_cars[i])):
            print("updated:", i, "speed:", speed, "lane:", l)

    # update road
    scroll += mc_car.speed
    if abs(scroll) > road.get_height():
        scroll = 0


    pygame.display.flip()

pygame.quit()