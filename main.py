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
#butterfly
triangle(-30,-30,45,70,"red",135,90,225)
square(-30,15,45,"green",90,180)
triangle(-76,60,45,70,"gold",135,90,135)
triangle(15,60,90,128,"blue",135,90,315)
triangle(106,148,90,128,"brown",135,90,45)
triangle(107,56,65,95,"cyan",135,90,0)
parallelogram(59,10,40,60,"pink",135,45,45)
#boat
square(-30,-30,45,"gold",90,180)
triangle(-30,15,45,70,"pink",135,90,45)
triangle(-27,17,65,95,"green",135,90,0)
triangle(15,-30,45,70,"blue",135,90,225)
parallelogram(63,16,45,70,"orange",135,45,135)
triangle(-63,16,90,128,"red",135,90,180)
triangle(-60,142,90,128,"magenta",135,90,90)

#code has been checked on the site https://metaschool.ru/pub/konkurs/python/turtle/index.php
#https://server.179.ru/tasks/python/2017b1/pgm12.5_Turtle.html - Main teams
#https://docs.python.org/2/library/turtle.html - turtle