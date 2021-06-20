"""
 The Logic Simulator

 The Logic Simulator uses graphical services
 provided by:
 
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
import Or
import Xor
import Nand
import Switch
import Bulb
 
# Define some colors
WHITE = (255, 255, 255)

gates = []
wires = []
mode = 3
gate0 = None
gate1 = None

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("The Logic Simulator")
icon = pygame.image.load("robot.bmp")
pygame.display.set_icon(icon)

# Pre-wiring section
a = Switch.Switch(20, 20, screen)
gates.append(a)
b = Switch.Switch(20, 40, screen)
gates.append(b)
x1 = Xor.Xor(50, 30, screen)
gates.append(x1)
a1 = And.And(50, 50, screen)
gates.append(a1)
wax1 = Wire.Wire(a, x1, screen)
wires.append(wax1)
wbx1 = Wire.Wire(b, x1, screen)
wires.append(wbx1)
waa1 = Wire.Wire(a, a1, screen)
wires.append(waa1)
wba1 = Wire.Wire(b, a1, screen)
wires.append(wba1)
bx1 = Bulb.Bulb(x1.endx, x1.y, screen)
gates.append(bx1)
x1.outpin.append(bx1)
cin = a1

offx = 90
a = Switch.Switch(offx+20, 20, screen)
gates.append(a)
b = Switch.Switch(offx+20, 40, screen)
gates.append(b)
x1 = Xor.Xor(offx+50, 30, screen)
gates.append(x1)
wax1 = Wire.Wire(a, x1, screen)
wires.append(wax1)
wbx1 = Wire.Wire(b, x1, screen)
wires.append(wbx1)
x2 = Xor.Xor(offx+90, 50, screen)
gates.append(x2)
wx1x2 = Wire.Wire(x1, x2, screen)
wires.append(wx1x2)
wcinx2 = Wire.Wire(cin, x2, screen)
wires.append(wcinx2)
a1 = And.And(offx+90, 80, screen)
gates.append(a1)
a2 = And.And(offx+90, 110, screen)
gates.append(a2)
wx1a1 = Wire.Wire(x1, a1, screen)
wires.append(wx1a1)
wcina1 = Wire.Wire(cin, a1, screen)
wires.append(wcina1)
waa2 = Wire.Wire(a, a2, screen)
wires.append(waa2)
wba2 = Wire.Wire(b, a2, screen)
wires.append(wba2)
o = Or.Or(offx+120, 95, screen)
gates.append(o)
wa1o = Wire.Wire(a1, o, screen)
wires.append(wa1o)
wa2o = Wire.Wire(a2, o, screen)
wires.append(wa2o)
bx2 = Bulb.Bulb(x2.endx, x2.y, screen)
gates.append(bx2)
x2.outpin.append(bx2)
cin = o

offx = 230
a = Switch.Switch(offx+20, 20, screen)
gates.append(a)
b = Switch.Switch(offx+20, 40, screen)
gates.append(b)
x1 = Xor.Xor(offx+50, 30, screen)
gates.append(x1)
wax1 = Wire.Wire(a, x1, screen)
wires.append(wax1)
wbx1 = Wire.Wire(b, x1, screen)
wires.append(wbx1)
x2 = Xor.Xor(offx+90, 50, screen)
gates.append(x2)
wx1x2 = Wire.Wire(x1, x2, screen)
wires.append(wx1x2)
wcinx2 = Wire.Wire(cin, x2, screen)
wires.append(wcinx2)
a1 = And.And(offx+90, 80, screen)
gates.append(a1)
a2 = And.And(offx+90, 110, screen)
gates.append(a2)
wx1a1 = Wire.Wire(x1, a1, screen)
wires.append(wx1a1)
wcina1 = Wire.Wire(cin, a1, screen)
wires.append(wcina1)
waa2 = Wire.Wire(a, a2, screen)
wires.append(waa2)
wba2 = Wire.Wire(b, a2, screen)
wires.append(wba2)
o = Or.Or(offx+120, 95, screen)
gates.append(o)
wa1o = Wire.Wire(a1, o, screen)
wires.append(wa1o)
wa2o = Wire.Wire(a2, o, screen)
wires.append(wa2o)
bx2 = Bulb.Bulb(x2.endx, x2.y, screen)
gates.append(bx2)
x2.outpin.append(bx2)
cin = o

offx = 370
a = Switch.Switch(offx+20, 20, screen)
gates.append(a)
b = Switch.Switch(offx+20, 40, screen)
gates.append(b)
x1 = Xor.Xor(offx+50, 30, screen)
gates.append(x1)
wax1 = Wire.Wire(a, x1, screen)
wires.append(wax1)
wbx1 = Wire.Wire(b, x1, screen)
wires.append(wbx1)
x2 = Xor.Xor(offx+90, 50, screen)
gates.append(x2)
wx1x2 = Wire.Wire(x1, x2, screen)
wires.append(wx1x2)
wcinx2 = Wire.Wire(cin, x2, screen)
wires.append(wcinx2)
a1 = And.And(offx+90, 80, screen)
gates.append(a1)
a2 = And.And(offx+90, 110, screen)
gates.append(a2)
wx1a1 = Wire.Wire(x1, a1, screen)
wires.append(wx1a1)
wcina1 = Wire.Wire(cin, a1, screen)
wires.append(wcina1)
waa2 = Wire.Wire(a, a2, screen)
wires.append(waa2)
wba2 = Wire.Wire(b, a2, screen)
wires.append(wba2)
o = Or.Or(offx+120, 95, screen)
gates.append(o)
wa1o = Wire.Wire(a1, o, screen)
wires.append(wa1o)
wa2o = Wire.Wire(a2, o, screen)
wires.append(wa2o)
bx2 = Bulb.Bulb(x2.endx, x2.y, screen)
gates.append(bx2)
x2.outpin.append(bx2)
bo = Bulb.Bulb(o.endx, o.y, screen)
gates.append(bo)
o.outpin.append(bo)

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
                for g in gates:
                    if isinstance(g, Switch.Switch):
                        g.update()
                        break
            elif event.key == pygame.K_b:
                mode = 4
            elif event.key == pygame.K_n:
                mode = 5
            elif event.key == pygame.K_o:
                mode = 6
            elif event.key == pygame.K_x:
                mode = 7
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
                            if isinstance(g, Bulb.Bulb):
                                print("gate0 NOT ALLOWED to be bulb!")
                                gate0 = None
                                break
                            gate0 = g
                            print("gate0 set!")
                        else:
                            gate1 = g
                            if isinstance(g, Switch.Switch):
                                print("gate1 NOT ALLOWED to be switch!")
                                gate0 = None
                                break
                            if isinstance(g, Bulb.Bulb):
                                print("gate1 NOT ALLOWED to be bulb!")
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
                        g.flick()
                        g.update()
                        break
            elif mode == 4:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        break
                if hit and (isinstance(g, And.And) or isinstance(g, Nand.Nand) or isinstance(g, Or.Or) or isinstance(g, Xor.Xor)):
                    gg = Bulb.Bulb(g.endx, g.y, screen)
                    gates.append(gg)
                    g.outpin.append(gg)
                else:
                    print("bulb can only be attached to logic gates!")
            elif mode == 5:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        break
                if not(hit):
                    g = Nand.Nand(pos[0], pos[1], screen)
                    gates.append(g)
            elif mode == 6:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        break
                if not(hit):
                    g = Or.Or(pos[0], pos[1], screen)
                    gates.append(g)
            elif mode == 7:
                hit = False
                for g in gates:
                    hit = g.updateInput(pos[0], pos[1])
                    if hit:
                        break
                if not(hit):
                    g = Xor.Xor(pos[0], pos[1], screen)
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
    for w in wires:
        w.render()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
