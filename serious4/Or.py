import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# OR Gate class
class Or():
    def __init__(self, x, y, screen):
        self.input0 = False
        self.input1 = False
        self.output = False
        self.pin0 = None
        self.pin1 = None
        self.outpin = []
        self.x = x
        self.y = y
        self.endx = x+29
        self.screen = screen

    def updateInput(self, x, y):
        hit = False
        if x > self.x and x < self.endx and y > self.y and y < self.y+18:
            hit = True
        return hit
        
    def update(self, state, pin):
        if pin == 0:
            self.input0 = state
        elif pin == 1:
            self.input1 = state
        else:
            print("pin violation!!!")
        self.output = self.input0 or self.input1
        for g in self.outpin:
            g.update(self.output)

    def render(self):
        pygame.draw.ellipse(self.screen, BLACK, [self.x-5, self.y, 16, 16], 1)
        pygame.draw.rect(self.screen, WHITE, [self.x-5, self.y, 8, 16])
        pygame.draw.line(self.screen, BLACK, [self.x+5, self.y], [self.x+10, self.y], 1)
        pygame.draw.line(self.screen, BLACK, [self.x+5, self.y+15], [self.x+10, self.y+15], 1)
        pygame.draw.arc(self.screen, BLACK, [self.x-8, self.y, 33, 12], 0, math.pi/2, 1)        
        pygame.draw.arc(self.screen, BLACK, [self.x-4, self.y+1,30,14], 3*math.pi/2, 2*math.pi, 1)        
        if self.input0:
            pygame.draw.line(self.screen, RED, [self.x, self.y+3], [self.x+7, self.y+3], 1)
        else:
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+3], [self.x+7, self.y+3], 1)

        if self.input1:
            pygame.draw.line(self.screen, RED, [self.x, self.y+12], [self.x+7, self.y+12], 1)
        else:
            pygame.draw.line(self.screen, BLACK, [self.x, self.y+12], [self.x+7, self.y+12], 1)

        if self.output:
            pygame.draw.line(self.screen, RED, [self.x+25, self.y+7], [self.x+28, self.y+7], 1)
        else:
            pygame.draw.line(self.screen, BLACK, [self.x+25, self.y+7], [self.x+28, self.y+7], 1)     
