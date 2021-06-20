import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Bulb class
class Bulb():
    def __init__(self, x, y, screen):
        self.output = False
        self.x = x
        self.y = y
        self.screen = screen

    def updateInput(self, x, y):
        hit = False
        if x > self.x and x < self.x+22 and y > self.y and y < self.y+18:
            hit = True
        return hit

    def update(self, state):
        self.output = state

    def render(self):
        if self.output:
            pygame.draw.ellipse(self.screen, RED, [self.x+6, self.y, 16, 16])
            pygame.draw.ellipse(self.screen, BLACK, [self.x+6, self.y, 16, 16], 1)
            pygame.draw.rect(self.screen, RED, [self.x, self.y+5, 8, 6])
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+5], [self.x+6, self.y+5], 1)
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+10], [self.x+6, self.y+10], 1)
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+5], [self.x, self.y+10], 1)
        else:
            pygame.draw.ellipse(self.screen, BLACK, [self.x+6, self.y, 16, 16], 1)
            pygame.draw.rect(self.screen, WHITE, [self.x+6, self.y+5, 6, 6])
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+5], [self.x+6, self.y+5], 1)
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+10], [self.x+6, self.y+10], 1)
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+5], [self.x, self.y+10], 1)
