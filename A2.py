print("############NEW RUN############")
# import libraries

import turtle
turtle.colormode(255)
import random
import tkinter as tk

# getting screen w and h
root = tk.Tk()
root.withdraw() 
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# making turtle screen
screen = turtle.Screen()
screen.setup(width, height)
screen.bgcolor("black")

# making turtles
t0 = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()
t9 = turtle.Turtle()
t10 = turtle.Turtle()


# FUNCTION to generate l-system instructions based on axiom and rules.
def create_l_system(iterations, axiom, rules):
    result = axiom
    for _ in range(iterations):
        new_string = ""
        for char in result:
            new_string += rules.get(char, char)
        result = new_string
    return result


## FUNCTION to set up turtle objects ##
# Parameters:
# - t: turtle object
# - coords: initial coordinates
# - turtle speed
def setup_turtle(t, coords, speed, size):
        t.hideturtle()
        t.pensize(size)
        t.speed(speed)  
        t.penup()
        t.goto(coords[0], coords[1])  
        t.pendown()
        print("setting up turtle")


# FUNCTION to assign colour to pen
def set_pen_color(c, t):
    t.pencolor(c[0], c[1], c[2])
    # print("setting pen colour")


# FUNCTION to draw l-system using turtle graphics
def draw_l_system(instructions, angle, distance, color, amt, size):

    stack0 = []
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    
    i = 1   # increment amount
    rInc, gInc, bInc = True, True, True
    
    r = color[0]
    g = color[1]
    b = color[2]

    # set up turtles
    for k in range(amt):
        turtle = globals().get(f't{k}')  # Access turtle t1, t2, etc. dynamically
        print(f't{k}')
        set_pen_color((r, g, b), turtle)
        setup_turtle(turtle, (random.randint(-300, 300), random.randint(-300, 300)), "fastest", size)

    ## loop runs for each instruction character
    for cmd in instructions:

        ## smoothly modifying colours ##
        if rInc:    # increment r value
          r +=i
          if r >= 255:
            r = 255
            rInc = False
        else:
          r -=i
          if r <= 0:
            r = 0
            rInc = True

        if gInc:    # increment g value
          g +=i
          if g >= 255:
            g = 255
            gInc = False
        else:
          g -=i
          if g <= 0:
            g = 0
            gInc = True

        if bInc:    # increment blue
          b +=i
          if b >= 255:
            b = 255
            bInc = False
        else:
          b -=i
          if b <= 0:
            b = 0
            bInc = True

        for k in range(amt):
            turtle = globals().get(f't{k}')  # Access turtle t1, t2, etc. dynamically
            if turtle:
                set_pen_color((r, g, b), turtle)

        ## drawing the L-system ##
        if cmd == 'F':  # Move forward and draw
            for k in range(amt):
                turtle = globals().get(f't{k}') 
                if turtle:
                    turtle.forward(distance)
            print("forward")

        elif cmd == 'f':  # Move forward without drawing
            for k in range(amt):
                turtle = globals().get(f't{k}')  
                if turtle:
                    turtle.penup()
                    turtle.forward(distance)
                    turtle.pendown()
            print("forward no draw")

        elif cmd == '+':  # Turn right
            for k in range(amt):
                turtle = globals().get(f't{k}') 
                if turtle:
                    turtle.right(angle)
            print("right")

        elif cmd == '-':  # Turn left
            for k in range(amt):
                turtle = globals().get(f't{k}') 
                if turtle:
                    turtle.left(angle)
            print("left")

        elif cmd == '[':  # Save current state (recursion)
            for k in range(amt):
                turtle = globals().get(f't{k}') 
                if turtle:
                    stack = globals().get(f'stack{k}')
                    print(f'stack{k}')
                    if stack:
                        stack.append((turtle.position(), turtle.heading()))
            print("save")

        elif cmd == ']':  # Restore previous state (recursion)
            for k in range(amt):
                stack = globals().get(f'stack{k}')
                if stack:
                    position, heading = stack.pop()
                    turtle = globals().get(f't{k}')
                    if turtle:
                        turtle.penup()
                        turtle.goto(position)
                        turtle.setheading(heading)
            print("previous state")
            
        # print("running", r)

    # Close the window on click
    screen.exitonclick()







## DRAWING

axiom = "+F"
# rules = {"F":"FF+FF+FF++"}

# rules = {"F":"FF+F-F"} #looks like cityscape

# rules = {"F":"F+F-F"} #looks like fractal-ish

# rules = {"F":"F[+FFFFF]-F+F"} #looks like buildingish

# rules = {
#    "F":"F+X-F",
#    "X":"F+[XXX]F-"
#    } 
# #looks like buildingish

# rules = {
#    "F":"+FX-FX",
#    "X":"F+[XXX]F-"
#    } 




# define L system grammar
gen_grammar = {
    'LSYSTEM': [["ACTION"]],
    'DELIMIT': [":"],
    'AXIOM': ["F"],
    'ACTION': ["F", "f", "-", "+"]
}

for i in range(random.randint(1,10)):
    gen_grammar['LSYSTEM'][0].append("ACTION")

# print(gen_grammar)


def generate(symbol, grammar):
    if isinstance(symbol, str) and symbol in grammar:
        production = random.choice(grammar[symbol])
        if isinstance(production, list):
            return ''.join(generate(sym, grammar) for sym in production)
        return production
    return symbol

rules_string = generate('LSYSTEM', gen_grammar)
print(rules_string)

rules_dict = {}
rules_dict[gen_grammar['AXIOM'][0]] = rules_string
print(rules_dict)




#returns all as list
# def generate(symbol, grammar):
#     result = []  # List to store the individual results
#     if isinstance(symbol, str) and symbol in grammar:
#         production = random.choice(grammar[symbol])  # Randomly choose a production
#         if isinstance(production, list):
#             for sym in production:
#                 result.extend(generate(sym, grammar))  
#         else:
#             result.append(production)
#     else:
#         result.append(symbol) 
#     return result



# rules = {"F":"F+X-F"}


iterations = random.randint(1, 8)
angle = random.randint(45, 90)
distance = random.randint(5, 20)

size = random.randint(1, 13)
amount = random.randint(1, 9)
# generate startcolor
startColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# make parameters into instructions
# instructions = create_l_system(iterations, axiom, rules)

   
# draw_l_system(instructions, angle, distance, startColor, amount, size)