import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Transistor class
class Trans():
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.input = False
        self.src = False
        self.output = True

    def render(self):
        pygame.draw.ellipse(self.screen, BLACK, [self.x+10, self.y+10, 50, 50], 1)
        if self.input:
            pygame.draw.line(self.screen, RED, [self.x+34, self.y+45], [self.x+34, self.y+80], 1)
            pygame.draw.line(self.screen, RED, [self.x+20, self.y+45], [self.x+48, self.y+45], 1)
        else:
            pygame.draw.line(self.screen, BLACK, [self.x+34, self.y+45], [self.x+34, self.y+80], 1)
            pygame.draw.line(self.screen, BLACK, [self.x+20, self.y+45], [self.x+48, self.y+45], 1)

        if self.src:
            pygame.draw.line(self.screen, RED, [self.x+28, self.y+45], [self.x+16, self.y+20], 1)
            pygame.draw.line(self.screen, RED, [self.x+0, self.y+20], [self.x+16, self.y+20], 1)
        else:
            pygame.draw.line(self.screen, BLACK, [self.x+28, self.y+45], [self.x+16, self.y+20], 1)
            pygame.draw.line(self.screen, BLACK, [self.x+0, self.y+20], [self.x+16, self.y+20], 1)

        if self.output:
            pygame.draw.line(self.screen, RED, [self.x+40, self.y+45], [self.x+50, self.y+25], 1)
            pygame.draw.polygon(self.screen, RED, [(self.x+53, self.y+27), (self.x+52, self.y+20), (self.x+47, self.y+23)])
            pygame.draw.line(self.screen, RED, [self.x+52, self.y+20], [self.x+68, self.y+20], 1)
        else:
            pygame.draw.line(self.screen, BLACK, [self.x+40, self.y+45], [self.x+50, self.y+25], 1)
            pygame.draw.polygon(self.screen, BLACK, [(self.x+53, self.y+27), (self.x+52, self.y+20), (self.x+47, self.y+23)])
            pygame.draw.line(self.screen, BLACK, [self.x+52, self.y+20], [self.x+68, self.y+20], 1)
