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
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = [60, 60, 60]
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1
        # fleet direction of 1 represents right; -1 is left
        self.fleet_direction = 1
