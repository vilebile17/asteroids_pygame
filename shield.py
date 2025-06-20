from collectables import Collectable
from constants import SHIELD_RADIUS, ITEM_RADIUS
from circleshape import CircleShape
import pygame

class ShieldItem(Collectable):
    # This class defines the structure of the shield item
    def __init__(self,x,y,radius):
        super().__init__(x,y,ITEM_RADIUS)
        self.image = pygame.transform.smoothscale(pygame.image.load("assets/Shield_texture.png"), (ITEM_RADIUS * 1.5, ITEM_RADIUS * 1.5))
    
    def draw(self,screen):
        screen.blit(self.image,(self.position.x,self.position.y))

    def update(self,dt):
        self.position += self.velocity * dt


class Shield(CircleShape):
    # This class defines the actual shield itself rather than the collectable
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"green",self.position,self.radius,1)
