import pygame
class Bullet:
    def __init__(self, x, y, to_x, to_y):
        self.pos = [x, y]
        self.to = [to_x, to_y]
        self.radius = 7
        self.color = (170, 0 , 0)
    
    def update_and_draw(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * self.to[0]) % width
        self.pos[1] = (self.pos[1] + dt * self.to[1]) % height
        
        pygame.draw.circle(screen, self.color, self.pos, self.radius)