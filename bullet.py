from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,SHOT_RADIUS)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,1)

    def update(self,dt):
        self.position += (self.velocity * dt)

