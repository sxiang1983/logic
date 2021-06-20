"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
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
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.ellipse(screen, BLACK, [10, 10, 50, 50], 1)
    pygame.draw.line(screen, BLACK, [20, 45], [48, 45], 1)
    pygame.draw.line(screen, BLACK, [34, 45], [34, 80], 1)
    pygame.draw.line(screen, BLACK, [40, 45], [50, 25], 1)
    pygame.draw.polygon(screen, BLACK, [(53, 27), (52, 20), (47, 23)])
    pygame.draw.line(screen, BLACK, [28, 45], [16, 20], 1)
    pygame.draw.line(screen, BLACK, [0, 20], [16, 20], 1)
    pygame.draw.line(screen, BLACK, [52, 20], [68, 20], 1)

    #pygame.draw.polygon(screen, BLACK, [(100, 100), (100, 105), (105, 105)])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
