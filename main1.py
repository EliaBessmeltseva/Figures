# Case 1
import turtle

def square(x, y, size, color, color2, angle):
    turtle.color(color)
    turtle.fillcolor(color2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.right(angle) # повернуть курсор на 90 градусов вправо
    turtle.pendown()
    for i in range(4):
        turtle.forward(size) # пройти вперед на насстояние 70, если курсор опущен, то будет нарисована линия
        turtle.right(angle)
    return()

def triangle(x, y, size1, size2, color, color2, angle1, angle2):
    turtle.color(color)
    turtle.fillcolor(color2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.right(angle1)
    turtle.pendown()
    turtle.forward(size1)
    turtle.right(angle2)
    turtle.forward(size1)
    turtle.right(angle1) # Повернуть курсор влево на 45 градусов
    turtle.forward(size2)
    return()

def parallelogram(x, y, size, color, angle):
    #TO DO: (Эля) функция рисов. параллелограмма
    pass
#(Настя) фигура дом, лебедь
#(Лера) фигура бабочка, лодка
#(Эля) фигура лиса, рыба