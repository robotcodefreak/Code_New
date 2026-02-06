import pygame
from sys import exit
from pygame.math import Vector2  # Proper import for Vector2

pygame.init()
screen = pygame.display.set_mode((1800, 1000))
clock = pygame.time.Clock()
pygame.display.set_caption("Game")

ground_rect = pygame.Rect(0, 900, 1800, 100)
gravity = 1.2

class Player:
    def __init__(self, x, y, width, height, color, controls, yspeed, xspeed):
        # Direction memory
        self.last_input_dir = "right"

        # Player data
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.controls = controls
        self.yspeed = yspeed    
        self.xspeed = xspeed
        self.basespeed = xspeed
        self.rect = pygame.Rect(x, y, width, height)
        self.onground = False

        # Dash system
        self.can_dash = True
        self.dash_cooldown = 400
        self.last_dash_time = 0
        self.dashing = False
        self.dash_time = 0
        self.dash_duration = 150
        self.dash_speed = 22
        self.dash_dir = Vector2(0, 0)
        
        # Sprinting
        self.sprintcd = 1000

    def handle_event(self, event):
        keys = pygame.key.get_pressed()

        # Input memory
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls["right"]:
                self.last_input_dir = "right"
            elif event.key == self.controls["left"]:
                self.last_input_dir = "left"

            # Dash trigger
            if event.key == pygame.K_x:
                current_time = pygame.time.get_ticks()
                if self.can_dash and not self.dashing:
                    self.can_dash = False
                    self.dashing = True
                    self.dash_time = current_time
                    self.last_dash_time = current_time
                    
                    self.dash_dir = Vector2(0, 0)
                    if keys[self.controls["right"]]:
                        self.dash_dir.x = 1
                    elif keys[self.controls["left"]]:
                        self.dash_dir.x = -1
                    else:
                        self.dash_dir.x = 1 if self.last_input_dir == "right" else -1

                    if self.dash_dir.length() != 0:
                        self.dash_dir = self.dash_dir.normalize()

        # If you let go of jump mid-air, smaller jump:
        if event.type == pygame.KEYUP and event.key == self.controls["up"]:
            if not self.onground and self.yspeed < -6:
                self.yspeed = -6

    def movement(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        # Sprint
        if keys[pygame.K_LSHIFT]:
            self.xspeed = self.basespeed * 1.6
        else:
            self.xspeed = self.basespeed

        move_dir = 0
        if keys[self.controls["left"]]:
            move_dir = -1
        if keys[self.controls["right"]]:
            move_dir = 1

        # 2. JUMP LOGIC (Hold to jump)
        # We put this outside the "if not self.dashing" if you want to jump immediately after a dash
        if keys[self.controls["up"]] and self.onground:
            self.yspeed = -20
            self.onground = False

        # 3. APPLY MOVEMENT
        if not self.dashing:
            self.rect.x += move_dir * self.xspeed
            
            # Apply Gravity
            self.yspeed += gravity
            self.rect.y += self.yspeed
        
        # 4. DASH MOVEMENT
        if self.dashing:
            self.rect.x += self.dash_dir.x * self.dash_speed
            self.rect.y += self.dash_dir.y * self.dash_speed
            
            if current_time - self.dash_time >= self.dash_duration:
                self.dashing = False
                self.yspeed = -3 

        # 5. DASH COOLDOWN
        if not self.can_dash and current_time - self.last_dash_time >= self.dash_cooldown and self.onground:
            self.can_dash = True

        # 6. GROUND COLLISION
        if self.rect.bottom >= 900:
            self.rect.bottom = 900
            self.yspeed = 0
            self.onground = True
        else:
            # Only set onground to false if we aren't currently in a dash 
            # (dashing often moves you slightly off the floor)
            if not self.dashing:
                self.onground = False

        # 7. SCREEN BOUNDARIES
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 1800:
            self.rect.right = 1800

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Player setup
player1 = Player(
    10, 850, 50, 50, (250, 0, 0),
    {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "down": pygame.K_DOWN, "up": pygame.K_UP},
    6, 6,
)

class Platform:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

platform1 = Platform(300, 700, 50, 200, (100,100,100))         

gameisrunning = True
# Main loop
while gameisrunning:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        player1.handle_event(event)

    player1.movement()
    player1.draw(screen)
    platform1.draw(screen)
    pygame.draw.rect(screen, (128, 128, 128), ground_rect)
    clock.tick(60)
    pygame.display.update()