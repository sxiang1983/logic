"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define current color
color = BLACK

# Wire class
class Wire():
    def __init__(self, begin, end, pin):
        self.begin = begin
        self.end = end
        self.pin = pin

    def update(self):
        if pin:
            self.end.input0 = self.begin.output
            self.end.update()
        else:
            self.end.input1 = self.begin.output
            self.end.update()

            
# AND Gate class
class And():
    def __init__(self, x, y):
        self.input0 = False
        self.input1 = False
        self.output = False
        self.x = x
        self.y = y

    def updateInput(self, x, y):
        hit = False
        if x > self.x and x < self.x+4 and y > self.y+1 and y < self.y+5:
            self.input0 = not(self.input0)
            hit = True
        if x > self.x and x < self.x+4 and y > self.y+10 and y < self.y+14:
            self.input1 = not(self.input1)
            hit = True
        return hit
        
    def update(self):
        self.output = self.input0 and self.input1

    def render(self):
        pygame.draw.ellipse(screen, BLACK, [self.x+5, self.y, 16, 16], 1)
        pygame.draw.rect(screen, WHITE, [self.x+5, self.y, 6, 16])
        pygame.draw.line(screen, BLACK, [self.x+4, self.y], [self.x+10, self.y], 1)
        pygame.draw.line(screen, BLACK, [self.x+4, self.y+15], [self.x+10, self.y+15], 1)
        pygame.draw.line(screen, BLACK, [self.x+4, self.y], [self.x+4, self.y+15], 1)
        
        self.update()
        if self.input0:
            pygame.draw.line(screen, RED, [self.x, self.y+3], [self.x+4, self.y+3], 1)
        else:
            pygame.draw.line(screen, BLACK, [self.x, self.y+3], [self.x+4, self.y+3], 1)

        if self.input1:
            pygame.draw.line(screen, RED, [self.x, self.y+12], [self.x+4, self.y+12], 1)
        else:
            pygame.draw.line(screen, BLACK, [self.x, self.y+12], [self.x+4, self.y+12], 1)

        if self.output:
            pygame.draw.line(screen, RED, [self.x+21, self.y+7], [self.x+24, self.y+7], 1)
        else:
            pygame.draw.line(screen, BLACK, [self.x+21, self.y+7], [self.x+24, self.y+7], 1)      
        
# Define an AND gate
gates = []

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("AND Gate")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            hit = False
            for g in gates:
                hit = g.updateInput(pos[0], pos[1])
                if hit:
                    break
            if not(hit):
                g = And(pos[0], pos[1])
                gates.append(g)
            
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    for g in gates:
        g.render()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
