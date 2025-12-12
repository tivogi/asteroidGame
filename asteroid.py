from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position.x, self.position.y),self.radius,LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ran_angle = random.uniform(20,50)
            ast1_velocity = self.velocity.rotate(ran_angle)
            ast2_velocity = self.velocity.rotate(- ran_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x,self.position.y,new_radius)
            ast2 = Asteroid(self.position.x,self.position.y , new_radius)
            ast1.velocity = ast1_velocity * 1.2
            ast2.velocity = ast2_velocity * 1.2
            
            