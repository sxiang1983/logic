"""
 The Logic Simulator

 
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import math
import Wire
import And
import Switch
 
# Define some colors
WHITE = (255, 255, 255)

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
            elif event.key == pygame.K_s:
                mode = 2
            elif event.key == pygame.K_r:
                mode = 3
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if mode == 0:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        break
                if not(hit):
                    g = And.And(pos[0], pos[1], screen)
                    gates.append(g)
            elif mode == 1:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        if gate0 == None:
                            gate0 = g
                            print("gate0 set!")
                        else:
                            gate1 = g
                            if isinstance(g, Switch.Switch):
                                print("gate1 NOT ALLOWED to be switch!")
                                gate0 = None
                                break
                            print("both gate0 and gate1 set!")
                            w = Wire.Wire(gate0, gate1, screen)
                            if w.pin != -1:
                                print("appended!")
                                wires.append(w)
                            gate0 = None
                            gate1 = None
                        break
            elif mode == 2:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        break
                if not(hit):
                    g = Switch.Switch(pos[0], pos[1], screen)
                    gates.append(g)
            elif mode == 3:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit and isinstance(g, Switch.Switch):
                        g.update()
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
