import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
    """Class that manages game assets and behavior"""

    def __init__(self):
        """Initialize the game and create the resources"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((self.settings.screen_length, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        #Set background color



    def run_game(self):
        """Start the main loop for the game"""
        self._check_events()
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            #self.screen.fill(self.settings.background_color)
            #make the most recently drawn screen visible
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)




    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _check_keydown_events(self, event):
        #Respond to key presses
        if event.key == pygame.K_RIGHT:
            # move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        # create the fleet of aliens
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        avail_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avail_space_x // (2 * alien_width)

        #create the first row of aliens
        for alien_number in range(number_aliens_x):
            #create an alien and place it in the row
            self._create_alien(alien_number)
    def _create_alien(self, alien_number):
        #create and alien and place it in a row
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()