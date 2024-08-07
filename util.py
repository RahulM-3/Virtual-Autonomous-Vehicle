import pygame

pygame.init()

green = (0, 255, 0)
red = (230, 16, 23)
gray = (133, 130, 130)


def debug(screen, texts, coords=(10, 10), font_size=25):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    x = coords[0]
    y = coords[1]
    for key, value in texts.items():
        renderkey = font.render(key+": ", True, green, gray)
        rendervalue = font.render(value, True, red, gray)
        screen.blit(renderkey, (x, y))
        x += renderkey.get_rect().right
        screen.blit(rendervalue, (x, y))
        x = coords[0]
        y += renderkey.get_rect().bottom