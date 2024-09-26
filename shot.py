from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)


    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

