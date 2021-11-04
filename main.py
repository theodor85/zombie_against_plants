import random

import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from zombie_against_grass import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    draw_background
)


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
draw_background(screen)


clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
