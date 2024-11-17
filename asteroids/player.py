from constants import *
from circleshape import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.PLAYER_SHOOT_COOLDOWN = PLAYER_SHOOT_COOLDOWN
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
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

        self.PLAYER_SHOOT_COOLDOWN -= dt

    def shoot(self):
        if self.PLAYER_SHOOT_COOLDOWN > 0:
            return
        self.PLAYER_SHOOT_COOLDOWN = 0.3
        velocity = pygame.math.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt