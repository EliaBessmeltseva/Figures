# Case 1
import turtle
def square(x, y, size, color, angle):
    #TO DO: (Настя) функция рисов. квадрата
    pass
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