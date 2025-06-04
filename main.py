import pygame, sys
from constants import *
from player import Player
from asteroid import *
from asteroidfield import AsteroidField

def main():
    pygame.init()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0

    print(asteroid_field in updatable)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit()
    
        pygame.display.flip()
        dt = time.tick(FPS) / 1000


if __name__ == "__main__":
    main()
