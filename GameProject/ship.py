import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        #Initilize the ship and set its starting postion
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ships horizonal pattern
        self.x = float(self.rect.x)


        #movement flags
        self.moving_right = False
        self.moving_left = False

        self.ship_speed = 1.5

    def update(self):
        # Update the ships postioin based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        #draw ship at the current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #center screen on ship
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
