import pygame
from sys import exit
from pygame.math import Vector2  # Proper import for Vector2

pygame.init()
screen = pygame.display.set_mode((1800, 1000))
clock = pygame.time.Clock()
pygame.display.set_caption("Game")

ground_rect = pygame.Rect(0, 900, 1800, 100)
gravity = 0.75

class Player:
    def __init__(self, x, y, width, height, color, controls, yspeed, xspeed):
        # Direction memory
        self.last_direction = "right"
        self.last_dash_direction = "right"
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
        self.rect = pygame.Rect(x, y, width, height)
        self.onground = False

        # Dash system
        self.can_dash = True
        self.dash_cooldown = 400
        self.last_dash_time = 0
        self.dashing = False
        self.dash_time = 0
        self.dash_duration = 300
        self.dash_speed = 13
        self.dash_dir = Vector2(0, 0)

    def handle_event(self, event):
        keys = pygame.key.get_pressed()

        # Input memory
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls["right"]:
                self.last_input_dir = "right"
            elif event.key == self.controls["left"]:
                self.last_input_dir = "left"

        # Jump
        if event.type == pygame.KEYDOWN and event.key == self.controls["up"] and self.onground:
            self.yspeed = -18
            self.onground = False
        elif event.type == pygame.KEYUP and event.key == self.controls["up"] and not self.onground:
            if self.yspeed < -6:
                self.yspeed = -6

        # Dash
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            current_time = pygame.time.get_ticks()
            if self.can_dash and not self.dashing:
                self.can_dash = False
                self.dashing = True
                self.dash_time = current_time
                self.last_dash_time = current_time

                # Set dash direction from last input
                self.dash_dir = Vector2(0, 0)
                if self.last_input_dir == "right":
                    self.dash_dir.x = 1
                elif self.last_input_dir == "left":
                    self.dash_dir.x = -1



                # Add any currently held key on the other axis for diagonal
                if keys[self.controls["right"]]:
                    self.dash_dir.x = 1
                elif keys[self.controls["left"]]:
                    self.dash_dir.x = -1

                # Normalize so diagonal speed matches
                if self.dash_dir.length() != 0:
                    self.dash_dir = self.dash_dir.normalize()

    def movement(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        # Normal movement
        if not self.dashing:
            if keys[self.controls["left"]]:
                self.rect.x -= self.xspeed
                self.last_direction = "left"
            if keys[self.controls["right"]]:
                self.rect.x += self.xspeed
                self.last_direction = "right"
            self.yspeed += gravity
            self.rect.y += self.yspeed

        # Dash movement
        if self.dashing:
            self.rect.x += self.dash_dir.x * self.dash_speed
            self.rect.y += self.dash_dir.y * self.dash_speed
            if current_time - self.dash_time >= self.dash_duration:
                self.dashing = False
                self.yspeed = 0

        # Dash cooldown
        if not self.can_dash and current_time - self.last_dash_time >= self.dash_cooldown and self.onground:
            self.can_dash = True
        #Platform Collision
        if Platform.is_solid == True and self.rect.colliderect(Platform.rect):
            ()# DO THIS TOMORROW
        if self.rect.bottom >= 900 and not self.dashing:
            self.rect.bottom = 900
            self.yspeed = 0
            self.onground = True
        else:
            self.onground = False

        # Screen boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 1800:
            self.rect.right = 1800

    # Drawing
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


# Player setup
player1 = Player(
    10, 850, 50, 50, (250, 0, 0),
    {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "down": pygame.K_DOWN, "up": pygame.K_UP},
    6, 6,
)
class Platform:
    def __init__(self, x, y, width, height, color, is_solid=True, one_way=False):
        self.x = x
        self.y =y
        self.rect = pygame.Rect(x, y, width, height)
        self.height= height
        self.width = width
        self.color = color
        self.is_solid = is_solid
        self.one_way = one_way
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
platform1 = Platform(300, 700, 50, 200, (100,100,100))         



# Main loop
while True:
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
