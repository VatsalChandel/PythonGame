import pygame

screen_width, screen_height = 800, 800

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (screen_width/2,screen_height/2))
        
    def update(self):
        self.rect.center = (pygame.mouse.get_pos()[0], 700)