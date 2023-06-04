import pygame
class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.pos = [x, y]
        self.to = [0, 0]
        self.acc = [0, 0]
        self.angle = 0
        
    def draw(self, screen):
        if self.to == [-1, -1]: 
            self.angle = 45
        elif self.to == [-1, 0]: 
            self.angle = 90
        elif self.to == [-1, 1]: 
            self.angle = 135
        elif self.to == [0, 1]: 
            self.angle = 180
        elif self.to == [1, 1]: 
            self.angle = -135
        elif self.to == [1, 0]: 
            self.angle = -90
        elif self.to == [1, -1]: 
            self.angle = -45
        elif self.to == [0, -1]: 
            self.angle = 0
        
        rotated = pygame.transform.rotate(self.image, self.angle)
        
        calib_pos = (self.pos[0] - rotated.get_width()/2,
                     self.pos[1] - rotated.get_height()/2)
        screen.blit(rotated, calib_pos)
        
    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt * 0.5) % width
        self.pos[1] = (self.pos[1] + dt * 0.3) % height
        
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y
    
    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = self.pos[0] + dt*self.to[0]
        self.pos[1] = self.pos[1] + dt*self.to[1]
        self.pos[0] = min(max(self.pos[0], 32), width-32)
        self.pos[1] = min(max(self.pos[1], 32), height-32)
