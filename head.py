import pygame
from pygame.sprite import Sprite

class Head(Sprite):
    '''A class to represent the head of your snake.'''

    def __init__(self, ai_settings, screen):
        '''Initialize the head and set its starting position.'''
        super(Head, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Begin in the center of the screen
        self.x = self.screen.get_rect().centerx
        self.y = self.screen.get_rect().centery
        self.color = (255, 255, 255)


        # # Create the head image, a circle
        # Set starting position to the center of the screen
        self.rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), 5)
        self.screen_rect = self.screen.get_rect()

        # Store a decimal value for the ship's center.
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)

        # Movement flags
        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Update the position of the head.'''
        # Unlike in alien invasion, the snake can't move diagonally, hence elif
        if self.moving_right:
            self.center_horizontal += self.ai_settings.head_speed_factor
        elif self.moving_left:
            self.center_horizontal -= self.ai_settings.head_speed_factor
        elif self.moving_up:
            self.center_vertical -= self.ai_settings.head_speed_factor
        elif self.moving_down:
            self.center_vertical += self.ai_settings.head_speed_factor

        self.rect.centerx = self.center_horizontal
        self.rect.centery = self.center_vertical

    def draw_head(self):
        '''Draw the head to the screen.'''
        pygame.draw.circle(self.screen, self.color, (self.rect.centerx, self.rect.centery), 5)
