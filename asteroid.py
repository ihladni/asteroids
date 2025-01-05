import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill() # temp

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # spawn 2 more
        angle = random.uniform(20, 50)

        vec1 = pygame.Vector2(self.velocity).rotate(angle)
        vec2 = pygame.Vector2(self.velocity).rotate(-angle)
        # ovo moze i krace vidim:
        # a = self.velocity.rotate(random_angle)
        # b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast1.velocity = vec1 * 1.2
        ast2.velocity = vec2 * 1.2
