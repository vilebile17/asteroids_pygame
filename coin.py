import pygame
from collectables import Collectable
from constants import ITEM_RADIUS, COIN_SCORE

class Coin(Collectable):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.image = pygame.transform.smoothscale(pygame.image.load("assets/Coin_texture.png"),(ITEM_RADIUS * 1.5, ITEM_RADIUS * 1.5))

    def update(self,dt):
        self.position += self.velocity * dt

    def draw(self,screen):
        screen.blit(self.image,(self.position.x,self.position.y))



