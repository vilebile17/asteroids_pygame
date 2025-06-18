import pygame
from circleshape import CircleShape 
from constants import *
from bullet import Shot
from shield import Shield

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.hitbox_radius = HITBOX_RADIUS
        self.rotation = 0
        self.x = x
        self.y = y
        self.timer = 0
        self.shield = []

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen,active_shield=False):
        pygame.draw.polygon(screen, "white",self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt * -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        for shield in self.shield:
            self.update_shield(shield)

    
    def out_of_bounds(self):
        if self.position[0] < -PLAYER_RADIUS or self.position[0] > SCREEN_WIDTH + PLAYER_RADIUS:
            return True
        if self.position[1] < -PLAYER_RADIUS or self.position[1] > SCREEN_HEIGHT + PLAYER_RADIUS:
            return True
        return False
    

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
            self.timer = PLAYER_SHOOT_COOLDOWN
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def shield_up(self):
        self.shield.append(  Shield(self.position.x,self.position.y,(SHIELD_RADIUS + 2 * len(self.shield) )  ) )
        print(self.shield)
        return True 

    def update_shield(self,shield):
        shield.position = self.position

        
