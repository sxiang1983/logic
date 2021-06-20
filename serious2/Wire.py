import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Wire class
class Wire():
    def __init__(self, begin, end, screen):
        self.begin = begin
        self.end = end
        self.pin = -1
        self.screen = screen
        self.hot = False
        if self.end.pin0 == None:
            self.end.pin0 = begin
            self.pin = 0
        elif self.end.pin1 == None:
            self.end.pin1 = begin
            self.pin = 1
        else:
            print("both pins taken!")
        if self.pin != -1:
            self.begin.outpin.append(self)

    def update(self, state):
        self.hot = state
        self.end.update(state, self.pin)
        
    def render(self):
        if self.pin == 0:
            if self.hot:
                pygame.draw.line(self.screen, RED, [self.begin.endx, self.begin.y+7], [self.end.x, self.end.y+3], 1)
            else:
                pygame.draw.line(self.screen, BLACK, [self.begin.endx, self.begin.y+7], [self.end.x, self.end.y+3], 1)
        elif self.pin == 1:
            if self.hot:
                pygame.draw.line(self.screen, RED, [self.begin.endx, self.begin.y+7], [self.end.x, self.end.y+12], 1)
            else:
                pygame.draw.line(self.screen, BLACK, [self.begin.endx, self.begin.y+7], [self.end.x, self.end.y+12], 1)
