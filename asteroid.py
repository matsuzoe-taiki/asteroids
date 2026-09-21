import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            "White",
            self.position,
            self.radius
        )
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        direction = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(direction) * 1.2
        seconds_velocity = self.velocity.rotate(-direction) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        seconds_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = first_velocity
        seconds_asteroid.velocity = seconds_velocity
