import pygame

def activate_lidar(color, radius):
    lidars = []
    while(radius >= 0):
        mask_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(mask_surface, color, (radius, radius), radius, 1)
        lidars.append(mask_surface)
        radius -= 30
    return lidars