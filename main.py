import pygame
from math import trunc
WHITE = (255, 255, 255)
GREEN = (1, 200, 1)
BROWN = (87, 62, 13)
pygame.init()
window = pygame.display.set_mode((800, 600))
window.fill(WHITE)
# Equations: vf = vi + at
# I could say: speed = speed - acceleration(time)

#  Maybe try changing the hitobx to be only on the bottom of the thing?


class Player:
    def __init__(self):
        self.x = 100
        self.y = 0
        self.hitbox = pygame.Rect(self.x, self.y + 50, 50, 1)
        self.air_time = 0
        pygame.draw.rect(window, GREEN, (self.x, self.y, 50, 50))

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        #self.hitbox = self.hitbox.move(x, y)
        window.fill(WHITE)
        pygame.draw.rect(window, GREEN, (self.x, self.y, 50, 50))

    def move_player(self, x, y):  # These are really the change in the x and y
        self.x += x
        self.y += y
        self.hitbox = self.hitbox.move(x, y)
        window.fill(WHITE)
        pygame.draw.rect(window, GREEN, (self.x, self.y, 50, 50))

    def gravity(self):
        if not self.hitbox.colliderect(ground.hitbox):   # will later change to checking if it collides with the ground
            self.move_player(0, 0 + 2 * self.air_time)
            self.air_time += .05
        else:
            self.air_time = 0
            self.set_pos(self.x, ground.y - 50)


class Ground:
    def __init__(self):
        self.y = 500
        self.hitbox = pygame.Rect(0, self.y, 800, 100)
        pygame.draw.rect(window, BROWN, (0, self.y, 800, 5))

    def blit(self):
        pygame.draw.rect(window, BROWN, (0, self.y, 800, 5))


player = Player()
ground = Ground()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    if not player.hitbox.colliderect(ground.hitbox):
        player.gravity()
    ground.blit()
    print player.hitbox
    print player.y
    pygame.display.flip()


