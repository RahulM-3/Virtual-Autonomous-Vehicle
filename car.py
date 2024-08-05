import pygame


class car(pygame.sprite.Sprite):
    def __init__(self, carfile, speed) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(carfile).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speed = speed
    
    def resize(self, height, width) -> None:
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = self.image.get_rect()
    
    def rotate(self, deg) -> None:
        self.image = pygame.transform.rotate(self.image, deg)
        self.rect = self.image.get_rect()
    
    def draw(self, screen, x, y) -> None:
        screen.blit(self.image, (x, y))
        self.rect.topleft = (x, y)
    
    def collision(self, object):
        return self.mask.overlap(object.mask, (object.rect.x - self.rect.x, object.rect.y - self.rect.y))