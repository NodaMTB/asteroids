import pygame
from constants import *
from circleshape import *
from asteroidfield import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius,):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        new_radius = int(self.radius - ASTEROID_MIN_RADIUS)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2