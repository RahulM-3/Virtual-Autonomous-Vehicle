import pygame

class lidar:
    def __init__(self, screen, coords):
        self.lidar_range = []
        self.screen = screen
        for i in range(8):
            lidar_img = pygame.image.load(f"images/lidar/green/{i}.png").convert_alpha()   
            lidar_mask = pygame.mask.from_surface(lidar_img)
            x = coords[0]-255
            y = coords[1]-250
            self.screen.blit(lidar_img, (x, y))
            self.lidar_range.append([lidar_mask, x, y])
        
    def get_data(self, object):
        collision_lidar = []
        for i, lidars in enumerate(self.lidar_range):
            collision = lidars[0].overlap(object.mask, (object.x - lidars[1], object.y - lidars[2]))
            if(collision):
                collision_lidar.append({i+1:collision})
                col_img = pygame.image.load(f"images/lidar/blue/{i}.png").convert_alpha()
                self.screen.blit(col_img, (lidars[1], lidars[2]))
        if(len(collision_lidar)):
            return collision_lidar
        return None