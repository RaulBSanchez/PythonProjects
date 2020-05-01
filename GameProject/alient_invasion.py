import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class that manages game assets and behavior"""

    def __init__(self):
        """Initialize the game and create the resources"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((self.settings.screen_length, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        #Set background color
        #self.color = [240, 140, 140]


    def run_game(self):
        """Start the main loop for the game"""
        
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #self.screen.fill(self.settings.background_color)
            #make the most recently drawn screen visible
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()