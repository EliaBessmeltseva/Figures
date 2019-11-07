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
#fish
triangle(0, -70, 90, 128, 'orange', 135, 90, 225)
triangle(90, 20, 90, 128, 'green', 135, 90, -45)
triangle(-2, 85, 45, 65, 'yellow', 135, 90, 45)
triangle(-47, -7, 45, 65, 'violet', 135, 90, 135)
square(-2, 38, 44, 'cyan', 90, 0)
parallelogram(-46, 38, 44, 60, 'blue', 135, 45, 45)
triangle(-90, 35, 60, 93, 'red', 135, 90, 90)
#fox
triangle(40, -34, 90, 128, 'orange', 135, 90, 45)
parallelogram(73, -155, 44, 60, 'blue', 135, 45, -90)
triangle(-24, 32, 90, 128, 'red', 135, 90, 90)
triangle(-26, -59, 65, 93, 'yellow', 135, 90, 270)
square(-57, 66, 44, 'cyan', 90, 45)
triangle(-90, 100, 45, 65, 'violet', 135, 90, 90)
triangle(-24, 36, 45, 65, 'green', 135, 90, 270)
#(Nastya) figure house, swan
#(Lera) figure butterfly, boat
#(Elia) figure fox, fish

#code has been checked on the site https://metaschool.ru/pub/konkurs/python/turtle/index.php
#https://server.179.ru/tasks/python/2017b1/pgm12.5_Turtle.html - Main teams
#https://docs.python.org/2/library/turtle.html - turtle