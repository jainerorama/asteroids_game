import pygame 
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot 

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_track = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()  
   

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = time_track.tick(59) / 1000    
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for objects in drawable:
            objects.draw(screen)
        pygame.display.flip()
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                  sys.exit("Game Over!")
        

if __name__ == "__main__":
    main()
