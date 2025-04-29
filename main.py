import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot

def main():

    #initialize game objects and dimensions
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0
    
    #game loop start
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update game state
        updateable.update(dt)

        #handle collision
        for asteroid in asteroids:
            if asteroid.collision_detect(player):
                print("Game Over")
                sys.exit()
            for shot in shots:
                if shot.collision_detect(asteroid):
                    shot.kill()
                    asteroid.split()

        #draw the screen and make background black
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen) 
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
