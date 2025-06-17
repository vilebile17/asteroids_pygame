from circleshape import CircleShape
import pygame

class Collectable(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)

    def collected(self):
        self.kill()
        return True
