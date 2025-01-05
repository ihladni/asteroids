import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    container = None
    shot_timer = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        super().__init__(x, y, PLAYER_RADIUS)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        # self.rotation += (PLAYER_TURN_SPEED * dt)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        
        self.shot_timer -= dt
        print(self.shot_timer)
        if self.shot_timer < 0:
            self.shot_timer = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shot_timer > 0:
            return

        new_shot = Shot(self.x, self.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        
