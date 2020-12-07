
class Settings():
    '''Settings for the game Snake.'''

    def __init__(self):
        # Screen settings
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (0, 0, 0)

        # Head settings
        self.head_color = (255, 255, 255)
        self.head_r = 5
        self.head_speed_factor = 3
