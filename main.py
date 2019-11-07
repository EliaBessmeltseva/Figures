# Case 1
import turtle

def square(x, y, size, color, angle, to_angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(to_angle)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(angle)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(angle)
        turtle.end_fill()
    return()
def triangle(x, y, size1, size2, color, angle1, angle2, to_angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(to_angle)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(angle1)
    turtle.pendown()
    turtle.forward(size1)
    turtle.right(angle2)
    turtle.forward(size1)
    turtle.right(angle1)
    turtle.forward(size2)
    turtle.end_fill()
    return()
def parallelogram(x, y, size1, size2, color, angle1, angle2, to_angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(to_angle)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(angle1)
    turtle.pendown()
    for i in range(2):
        turtle.forward(size1)
        turtle.right(angle1)
        turtle.forward(size2)
        turtle.right(angle2)
    turtle.end_fill()
    return()
#(Nastya) figure house, swan
#(Lera) figure butterfly, boat
#(Elia) figure fox, fish

#code has been checked on the site https://metaschool.ru/pub/konkurs/python/turtle/index.php
#https://server.179.ru/tasks/python/2017b1/pgm12.5_Turtle.html - Main teams
#https://docs.python.org/2/library/turtle.html - turtle