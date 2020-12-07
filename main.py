import pygame
from head import Head
from settings import Settings
import game_functions as gf


def main():
    '''Main function of Snake.'''

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption('Snake')
    head = Head(ai_settings, screen)

    while True:
        # Check events
        gf.check_events()

        #
        head.update()

        # Update the items drawn on the screen
        screen.fill(ai_settings.bg_color)
        head.draw_head()
        pygame.display.flip()

# Run game
main()
