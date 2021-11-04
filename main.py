import random

import pygame
from pygame.constants import (
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
    draw_background,
    Zombie,
)


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()

ADDZOMBIE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDZOMBIE, 3000)

zombies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDZOMBIE:
            new_zombie = Zombie()
            zombies.add(new_zombie)
            all_sprites.add(new_zombie)

    draw_background(screen)
    zombies.update()
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
