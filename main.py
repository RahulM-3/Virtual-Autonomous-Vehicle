# imports
import pygame
from math import ceil
from random import randint
from car import car

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
mc_car = car(r"images/mc-car.png", 0.1)
mc_car.resize(60, 110)
pos = 200
mc_car_group = pygame.sprite.Group()
mc_car_group.add(mc_car)

# npc car sprite
npc1 = car(r"images/car1.png", 0.05)
npc1.resize(50, 100)
npcpos = pos+200
npc_car_group = pygame.sprite.Group()
npc_car_group.add(npc1)

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
    
    # draw car
    mc_car.draw(screen, 320, pos)
    npc1.draw(screen, 325, npcpos)
    npcpos -= mc_car.speed-npc1.speed
    #if(mc_car.collision(npc1)):
    #if(pygame.sprite.spritecollide(mc_car, npc_car_group, False, pygame.sprite.collide_mask)):
    if(pygame.Rect.colliderect(mc_car.rect, npc1.rect)):
        print("Collision")

    # update road
    scroll += mc_car.speed
    if abs(scroll) > road.get_height():
        scroll = 0

    
    pygame.display.flip()

pygame.quit()