import pygame, sys
from player import Player

screen_width, screen_height = 800, 800


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_visible(False)


player = Player() 
player_group = pygame.sprite.Group()
player_group.add(player) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() 
            
    screen.fill((30,30,30))
    player_group.draw(screen)
    player_group.update()
    pygame.display.flip()
    clock.tick(30)