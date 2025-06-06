import pygame
from circleshape import CircleShape 
from constants import *
from bullet import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.hitbox_radius = HITBOX_RADIUS
        self.rotation = 0
        self.x = x
        self.y = y
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen,show_hitboxes=False):
        pygame.draw.polygon(screen, "white",self.triangle(), 2)
        if show_hitboxes:
            pygame.draw.circle(screen, "red", self.position, self.hitbox_radius, 1)

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
    
    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
            self.timer = PLAYER_SHOOT_COOLDOWN
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        
