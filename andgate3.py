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

# AND Gate class
class And():
    def __init__(self):
        self.input0 = False
        self.input1 = False
        self.output = False

    def update(self):
        self.output = self.input0 and self.input1

# Define an AND gate
a0 = And()

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

x = 200
y = 200
 
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
            if pos[0] > x and pos[0] < x+4 and pos[1] > y+1 and pos[1] < y+5:
                a0.input0 = not(a0.input0)
            if pos[0] > x and pos[0] < x+4 and pos[1] > y+10 and pos[1] < y+14:
                a0.input1 = not(a0.input1)
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.ellipse(screen, BLACK, [x+5, y, 16, 16], 1)
    pygame.draw.rect(screen, WHITE, [x+5, y, 6, 16])
    pygame.draw.line(screen, BLACK, [x+4, y], [x+10, y], 1)
    pygame.draw.line(screen, BLACK, [x+4, y+15], [x+10, y+15], 1)
    pygame.draw.line(screen, BLACK, [x+4, y], [x+4, y+15], 1)
    
    a0.update()
    if a0.input0:
        pygame.draw.line(screen, RED, [x, y+3], [x+4, y+3], 1)
    else:
        pygame.draw.line(screen, BLACK, [x, y+3], [x+4, y+3], 1)

    if a0.input1:
        pygame.draw.line(screen, RED, [x, y+12], [x+4, y+12], 1)
    else:
        pygame.draw.line(screen, BLACK, [x, y+12], [x+4, y+12], 1)

    if a0.output:
        pygame.draw.line(screen, RED, [x+21, y+7], [x+24, y+7], 1)
    else:
        pygame.draw.line(screen, BLACK, [x+21, y+7], [x+24, y+7], 1)      
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
