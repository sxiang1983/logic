import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Switch class
class Switch():
    def __init__(self, x, y, screen):
        self.output = False
        self.outpin = []
        self.x = x
        self.y = y
        self.screen = screen

    def updateInput(self, x, y):
        hit = False
        if x > self.x and x < self.x+22 and y > self.y and y < self.y+18:
            hit = True
        return hit

    def update(self):
        self.output = not(self.output)
        for g in self.outpin:
            g.update(self.output)

    def render(self):
        if self.output:
            pygame.draw.ellipse(self.screen, BLACK, [self.x, self.y, 18, 18], 1)
            pygame.draw.ellipse(self.screen, RED, [self.x+3, self.y+3, 13, 13])
            pygame.draw.line(self.screen, RED, [self.x+18, self.y+8], [self.x+24, self.y+8], 1)
        else:
            pygame.draw.ellipse(self.screen, BLACK, [self.x, self.y, 18, 18], 1)
            pygame.draw.line(self.screen, BLACK, [self.x+18, self.y+8], [self.x+24, self.y+8], 1)

