from circleshape import CircleShape
from constants import *
import pygame, random


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)

    def draw(self,screen): 
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            direction_of_split = random.uniform(20,50)
            vector1 = self.velocity.rotate(direction_of_split)
            vector2 = self.velocity.rotate(-direction_of_split)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            daughter_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            daughter_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            daughter_asteroid1.velocity = vector1 * 1.2
            daughter_asteroid2.velocity = vector2 * 1.2

            



