# import libraries

import turtle
turtle.colormode(255)
import random

import tkinter as tk

# Create a root window (hidden)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Get screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Create a screen object
screen = turtle.Screen()
screen.setup(width, height)
screen.tracer(0)  # Disable automatic screen updates for manual control
screen.bgcolor("black")



# Create a turtle object
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()


# FUNCTION to generate l-system instructions based on axiom and rules.
def create_l_system(iterations, axiom, rules):
    result = axiom
    for _ in range(iterations):
        new_string = ""
        for char in result:
            new_string += rules.get(char, char)
        result = new_string
    return result


# FUNCTION to assign colour to pen
def set_pen_color(c, t):
    t.pencolor(c[0], c[1], c[2])


# Draw the L-System using turtle graphics.
# Parameters:
# - instructions: string of L-System commands
# - angle: turning angle in degrees
# - distance: forward movement distance

def draw_l_system(instructions, angle, distance, color, turtle):
    stack = []  # for saving previous state

    t = turtle 
    
    i = 1
    rInc, gInc, bInc = True, True, True
    
    sizeInc = True
    penSize = 4
    
    # speedInc = True
    # penSpeed = "fastest"
    
    r = color[0]
    g = color[1]
    b = color[2]

    for cmd in instructions:

        ## smoothly modifying colours ##
        # increment r value
        if rInc:
          r +=i
          if r >= 255:
            r = 255
            rInc = False
        else:
          r -=i
          if r <= 0:
            r = 0
            rInc = True

        # increment g value
        if gInc:
          g +=i
          if g >= 255:
            g = 255
            gInc = False
        else:
          g -=i
          if g <= 0:
            g = 0
            gInc = True

        # increment blue
        if bInc:
          b +=i
          if b >= 255:
            b = 255
            bInc = False
        else:
          b -=i
          if b <= 0:
            b = 0
            bInc = True

        set_pen_color((r, g, b), t)


        # ## randomly adjusting pen size ##
        # chance = random.randint(0, 5)
        
        # if sizeInc == True:
        #         penSize += i
        #         # penSpeed +=i
        #         if penSize >= 13:
        #             penSize = 13
        #             sizeInc = False
        #             print("inc: ",penSize)
        # else:
        #         penSize -= i
        #         # penSpeed -= i
        #         if penSize <= 4:
        #             penSize = 4
        #             sizeInc = True
        #             print("dec: ",penSize)
                    
        # if chance > 3:
        #     i = random.randint(0, 1)
            
        # t.pensize(penSize)
        
        # if penSpeed >= 20:
        #     penSpeed = 20
        # elif penSpeed <= 13:
        #     penSpeed = 13
            
        # t.speed("fastest")  
        

        ## drawing the L-system ##
        if cmd == 'F':  # Move forward and draw
            t.forward(distance)
        elif cmd == 'f':  # Move forward without drawing
            t.penup()
            t.forward(distance)
            t.pendown()
        elif cmd == '+':  # Turn right
            t.right(angle)
        elif cmd == '-':  # Turn left
            t.left(angle)
        elif cmd == '[':  # Save current state (recursion)
            stack.append((t.position(), t.heading()))
        elif cmd == ']':  # Restore previous state (recursion)
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()
            
        print("running", r)

    # Close the window on click
    screen.exitonclick()

def setup_turtle(t, coords, speed):
        t.hideturtle()
        t.speed(speed)  # Fastest speed
        t.penup()
        t.goto(coords[0], coords[1])  # Start position
        t.pendown()
        print("setting up turtle")
        print(coords)


## ACTUAL USE

# koch
# axiom = "F"
# rules = {"F" : "F+F-F-F+F"}
# iterations = 4
# angle = 90
# lineSize = 10

# sierpinski triangle
# axiom = "F-G-G"
# rules = {"F" : "F-G+F+G-F", "G" : "GG"}
# iterations = 5
# angle = 120
# lineSize = 10

# dragon curve
# axiom = "FX"
# rules = {
#     "X":"X+YF+",
#     "Y":"-FX-Y"
# }
# angle = 90
# iterations = 12
# lineSize = 20

# axiom = "F-G"
# rules = {
#     "F" : "F-G+F+G-F", 
#     "G" : "GG+F"
# }

# AS OF NOW
# axiom = "F-G-F"
# rules = {
#     "F" : "G+G-G+G+G-G", 
#     "G" : "FF"
# }

axiom = "F"
rules = {"F":"FF+FF+FF++"}
iterations = 1
angle = 75
scale = 10


setup_turtle(t1, (0, 0), 13)
setup_turtle(t2, (200, 0), 13)
setup_turtle(t3, (-200, -0), 13)


# make parameters into instructions
instructions = create_l_system(iterations, axiom, rules)

# generate startcolor
startColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# draw l system
draw_l_system(instructions, angle, scale, startColor, t1)
draw_l_system(instructions, angle, scale, startColor, t2)
draw_l_system(instructions, angle, scale, startColor, t3)

screen.update()


# for i in range(5):
#   t.pensize(i+1)
#   draw_l_system(instructions, angle, i)
