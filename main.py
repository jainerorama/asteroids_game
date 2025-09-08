import pygame 
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
from textdisplay import TextDisplay

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
    base_font = pygame.font.SysFont(None,16)
    font = pygame.font.SysFont("comicsans",30)
    score = 0
    score_board = TextDisplay("Score: ",0,font, True, (255,255,255), 20,20)

   # def draw_count(text,font,text_col,x,y):


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = time_track.tick(59) / 1000    
        screen.fill((0, 0, 0))
        updatable.update(dt)
        score_board.draw(screen) 
        for objects in drawable:
            objects.draw(screen)
        pygame.display.flip()
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                  sys.exit("Game Over!")
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score += 1
                    score_board.update_value(score)
        

if __name__ == "__main__":
    main()
