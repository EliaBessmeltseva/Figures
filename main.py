# Case 1
import turtle


def square(x, y, size, color, angle, to_angle):         # Nastya
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


def triangle(x, y, size1, size2, color, angle1, angle2, to_angle):          # Lera
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


def parallelogram(x, y, size1, size2, color, angle1, angle2, to_angle):         # Elia
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


triangle(-300, 140, 90, 128, 'orange', 135, 90, 225)         # Fish (Elia)
triangle(-210, 230, 90, 128, 'green', 135, 90, -45)
triangle(-302, 295, 45, 65, 'yellow', 135, 90, 45)
triangle(-346, 203, 45, 65, 'violet', 135, 90, 135)
square(-301, 248, 44, 'cyan', 90, 0)
parallelogram(-347, 248, 44, 60, 'blue', 135, 45, 45)
triangle(-390, 245, 60, 85, 'red', 135, 90, 90)


triangle(-260, -244, 90, 128, 'orange', 135, 90, 45)         # Fox (Elia)
parallelogram(-227, -275, 44, 60, 'blue', 135, 45, -90)
triangle(-324, -178, 90, 128, 'red', 135, 90, 90)
triangle(-326, -269, 65, 93, 'yellow', 135, 90, 270)
square(-357, -144, 44, 'cyan', 90, 45)
triangle(-390, -110, 45, 65, 'violet', 135, 90, 90)
triangle(-324, -175, 45, 65, 'green', 135, 90, 270)


triangle(-30,-30,45,70,"red",135,90,225)         # Butterfly (Lera)
square(-30,15,45,"green",90,180)
triangle(-76,60,45,70,"gold",135,90,135)
triangle(15,60,90,128,"blue",135,90,315)
triangle(106,148,90,128,"brown",135,90,45)
triangle(107,56,65,95,"cyan",135,90,0)
parallelogram(59,10,40,60,"pink",135,45,45)


square(-30,-30,45,"gold",90,180)         # Boat (Lera)
triangle(-30,15,45,70,"pink",135,90,45)
triangle(-27,17,65,95,"green",135,90,0)
triangle(15,-30,45,70,"blue",135,90,225)
parallelogram(63,16,45,70,"orange",135,45,135)
triangle(-63,16,90,128,"red",135,90,180)
triangle(-60,142,90,128,"magenta",135,90,90)


square(-43, 113, 35, 'cyan', 90, 0)         # House (Nastya)
parallelogram(-78, 75, 35, 60, 'pink', 135, 45, -225)
triangle(30, 30, 45, 65, 'red', 135, 90, 0)
triangle(32, -34, 45, 65, 'yellow', 135, 90, 270)
triangle(-100, -34, 90, 128, 'blue', 135, 90, 180)
triangle(-80, 33, 90, 128, 'orange', 135, 90, 180)
triangle(-100, -34, 64, 70, 'green', 135, 90, 225)


square(-82, 43, 43, 'blue', 90, 45)         # Swan (Nastya)
parallelogram(-82, 45, 60, 45, 'purple', 135, 45, 225)
triangle(-85, 106, 45, 65, 'red', 135, 90, 45)
triangle(-114, 13, 45, 65, 'cyan', 135, 90, 90)
triangle(60, -10, 90, 128, 'orange', 135, 90, 0)
triangle(20, -100, 90, 128, 'green', 135, 90, -45)
triangle(-70, -100, 64, 70, 'yellow', 135, 90, 270)


turtle.done()