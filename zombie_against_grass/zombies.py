import random
from enum import Enum
from typing import List, Dict

import pygame
from pygame.sprite import Sprite
from pygame.constants import (
    RLEACCEL,
)

from .background import (
    CELL_HEIGHT, CELL_WIDTH, FIELD_WIDTH, FIELD_HEIGHT, TOP_LEFT_FIELD_CORNER
)


class Zombie(Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.zombie_type = ZombieType(random.randint(0, len(ZombieType) - 1))
        self.sprite_path = next(
                filter(lambda t: t['type'] == self.zombie_type, ZombieParams)
            )['sprite_path']
        self.surf = pygame.image.load(self.sprite_path).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(FIELD_WIDTH + 90, FIELD_WIDTH + 100),
                ZombieStartPoints[random.randint(0, 4)],
            )
        )
        self.speed = next(
                filter(lambda t: t['type'] == self.zombie_type, ZombieParams)
            )['speed']

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < TOP_LEFT_FIELD_CORNER[0]:
            self.kill()


class ZombieType(Enum):
    FIRST = 0
    SECOND = 1
    THIRD = 2


ZombieParams: List[Dict] = [{
        'type': ZombieType.FIRST,
        'sprite_path': 'images/sprites/zombies/first.png',
        'speed': 2
    },
    {
        'type': ZombieType.SECOND,
        'sprite_path': 'images/sprites/zombies/second.png',
        'speed': 5
    },
    {
        'type': ZombieType.THIRD,
        'sprite_path': 'images/sprites/zombies/third.png',
        'speed': 6
    },
]


ZombieStartPoints = [
    TOP_LEFT_FIELD_CORNER[1] +
    int(CELL_HEIGHT / 2) + CELL_HEIGHT * i for i in range(5)
]
