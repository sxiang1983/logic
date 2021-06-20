import pygame

# Define some colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Wire class
class Wire():
    def __init__(self, begin, end, screen):
        self.begin = begin
        self.end = end
        self.screen = screen
        self.hot = False
        self.begin.outpin.append(self)

    def update(self, state):
        self.hot = state
        self.end.update(state)
        
    def render(self):
        if self.hot:
            pygame.draw.line(self.screen, RED, [self.begin.cx, self.begin.cy], [self.end.cx, self.end.cy], 1)
        else:
            pygame.draw.line(self.screen, BLACK, [self.begin.cx, self.begin.cy], [self.end.cx, self.end.cy], 1)
