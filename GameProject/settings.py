class Settings:
    """A class to store all settings for the game"""
    def __init__(self):
        """Initial Game Settings"""
        # Screen settings
        self.bg_color = [230, 230, 230]
        self.screen_width = 1000
        self.screen_length = 400
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = [60, 60, 60]