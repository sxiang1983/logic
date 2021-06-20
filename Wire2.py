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
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.pin = -1
        if self.end.pin0 == None:
            self.end.pin0 = begin
            self.pin = 0
        elif self.end.pin1 == None:
            self.end.pin1 = begin
            self.pin = 1
        else:
            print("both pins taken!")
        self.begin.outpin.append(end)

    def render(self):
        if (self.pin == 0):
            pygame.draw.line(screen, BLACK, [self.begin.x+24, self.begin.y+7], [self.end.x, self.end.y+3], 1)
        elif (self.pin == 1):
            pygame.draw.line(screen, BLACK, [self.begin.x+24, self.begin.y+7], [self.end.x, self.end.y+12], 1)

            
# AND Gate class
class And():
    def __init__(self, x, y):
        self.input0 = False
        self.input1 = False
        self.output = False
        self.pin0 = None
        self.pin1 = None
        self.outpin = []
        self.x = x
        self.y = y

    def updateInput(self, x, y):
        hit = False
        if x > self.x and x < self.x+22 and y > self.y and y < self.y+18:
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
        
gates = []
wires = []
mode = 0
gate0 = None
gate1 = None

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mode = 0
            elif event.key == pygame.K_w:
                mode = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            if mode == 0:
                pos = pygame.mouse.get_pos()
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        break
                if not(hit):
                    g = And(pos[0], pos[1])
                    gates.append(g)
            elif mode == 1:
                pos = pygame.mouse.get_pos()
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        if gate0 == None:
                            gate0 = g
                        else:
                            gate1 = g
                            print("both gate0 and gate1 set!")
                            w = Wire(gate0, gate1)
                            if w.pin != -1:
                                print("appended!")
                                wires.append(w)
                            gate0 = None
                            gate1 = None
                        break
               

 
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
    for w in wires:
        w.render()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
