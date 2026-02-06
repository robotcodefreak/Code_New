import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display (1000x800 windowed)
screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fighting Frenzy")

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60


# Main loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    
    
    
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
