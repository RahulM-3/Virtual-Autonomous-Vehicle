import pygame

class car(pygame.sprite.Sprite):
    def __init__(self, carfile, speed, x, y, x2=-1, lane=0) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(carfile).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.x = x
        self.y = y
        self.x2 = x2
        self.lane = lane
        self.rotated = False
    
    def resize(self, height, width) -> None:
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    
    def rotate(self, deg) -> None:
        self.image = pygame.transform.rotate(self.image, deg)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self, screen) -> None:
        if(self.lane==0):
            if(self.rotated):
                self.rotate(180)
                self.rotated = False
            screen.blit(self.image, (self.x, self.y))
            self.rect.topleft = (self.x, self.y)
        else:
            if(not self.rotated):
                self.rotate(180)
                self.rotated = True
            screen.blit(self.image, (self.x2, self.y))
            self.rect.topleft = (self.x2, self.y)
        
    def collision(self, object):
        return self.mask.overlap(object.mask, (object.rect.x - self.rect.x, object.rect.y - self.rect.y))