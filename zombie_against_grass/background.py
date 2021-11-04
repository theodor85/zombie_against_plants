import pygame


SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 940

FIELD_WIDTH = SCREEN_WIDTH - 252  # 1248
FIELD_HEIGHT = SCREEN_HEIGHT - 130  # 810

BACKGROUND_COLOR = (0x62, 0xC3, 0x70)
FIELD_COLOR = (0x27, 0x68, 0x31)
CELL_BORDER = (0x16, 0x3B, 0x1C)


def draw_background(screen: pygame.surface.Surface) -> None:
    screen.fill(BACKGROUND_COLOR)
    # game field
    pygame.draw.rect(
        screen,
        FIELD_COLOR,
        (
            200,
            80,
            FIELD_WIDTH,
            FIELD_HEIGHT,
        ),
    )
    for i in range(8):
        for j in range(5):
            pygame.draw.rect(
                screen,
                CELL_BORDER,
                (
                    200 + i*156,
                    80 + j*162,
                    156,
                    162,
                ),
                width=1,
            )
