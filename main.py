import pygame, sys
from constants import *
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
from bullet import Shot
from scoring import total_score
from shield import ShieldItem, Shield
from coin import Coin

def main():
    pygame.init()

    total_frames = 0
    active_shield = False
    num_coins_collected = 0

    collectable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    ShieldItem.containers = (updatable,drawable,collectable)
    Coin.containers = (updatable,drawable,collectable)
    Shield.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (updatable,drawable,bullets)
    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    
    kill_count = 0
    shield = None

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
        
        collided_asteroids = set()
        collided_bullets = set()
        for asteroid in asteroids:
            if asteroid.colliding(player) or player.out_of_bounds():
                print("Game over!")
                print(f"you got a score of {score}, Well Done!")
                sys.exit()
            elif active_shield:
                if player.shield[-1].colliding(asteroid):
                    player.shield[-1].kill()
                    player.shield.pop()
                    if len(player.shield) == 0:
                        active_shield = False
                    collided_asteroids.add(asteroid)
            for bullet in bullets:
                if asteroid.colliding(bullet):
                    collided_asteroids.add(asteroid)
                    collided_bullets.add(bullet)

        for asteroid in collided_asteroids:
            kill_count += 1
            kill_count = asteroid.split(kill_count)
        for bullet in collided_bullets:
            bullet.kill()
        
        collected_coin = False
        for item in collectable:
            if item.colliding(player):
                item.collected()
                if isinstance(item,ShieldItem):
                    active_shield = player.shield_up()
                elif isinstance(item,Coin):
                    num_coins_collected += 1
                    

        total_frames += 1
        score = total_score(total_frames,kill_count,num_coins_collected)
        font = pygame.font.SysFont(FONT, FONT_SIZE)
        text = font.render(f"SCORE: {score}",True, "white")
        text_rect = text.get_rect(topright=(SCREEN_WIDTH,0))
        screen.blit(text,text_rect)

    
        pygame.display.flip()
        dt = time.tick(FPS) / 1000


if __name__ == "__main__":
    main()
