import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock() 
pygame.display.set_caption("PygameTutorial")
test_surface = pygame.Surface((100,200))
test_surface.fill((255,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(200,100))
    pygame.display.update()



    clock.tick(60)