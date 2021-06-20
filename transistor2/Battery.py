import pygame

# Define some colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Battery class
class Battery():
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.output = True
        self.outpin = []

    def updatesrc(self, src):
        for g in self.outpin:
            g.update(self.output)
            
    def render(self):
        pygame.draw.ellipse(self.screen, RED, [self.x+10, self.y+10, 30, 10], 1)
        pygame.draw.line(self.screen, RED, [self.x+10, self.y+15], [self.x+10, self.y+60])
        pygame.draw.line(self.screen, RED, [self.x+39, self.y+15], [self.x+39, self.y+60])
        pygame.draw.ellipse(self.screen, RED, [self.x+10, self.y+55, 30, 10], 1)
        pygame.draw.rect(self.screen, WHITE, [self.x+11, self.y+55, 28, 5])
        pygame.draw.line(self.screen, RED, [self.x+25, self.y+25], [self.x+25, self.y+29])
        pygame.draw.line(self.screen, RED, [self.x+23, self.y+27], [self.x+27, self.y+27])
        pygame.draw.line(self.screen, RED, [self.x+23, self.y+55], [self.x+27, self.y+55])
        pygame.draw.line(self.screen, RED, [self.x+25, self.y+15], [self.x+25, self.y+5])
