from turtle import *

# Функции для рисования жирафа
def draw_leg():
    for _ in range(2):
        my_turtle.forward(50)
        my_turtle.right(90)
        my_turtle.forward(200)
        my_turtle.right(90)

def draw_body():
    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.forward(300)
    my_turtle.right(90)
    my_turtle.forward(200)
    my_turtle.right(90)
    my_turtle.forward(300)
    my_turtle.right(90)

def draw_neck():
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)

def draw_head():
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)

def draw_ear():
    my_turtle.forward(30)
    my_turtle.left(90)
    my_turtle.forward(30)
    my_turtle.right(90)
    my_turtle.forward(30)
    my_turtle.right(90)
    my_turtle.forward(30)
    my_turtle.left(90)

# Инициализация черепахи
my_turtle = Turtle()
my_turtle.speed(1)
my_turtle.penup()
my_turtle.goto(-150, -200)
my_turtle.pendown()

# Рисуем жирафа
draw_leg()            # Рисуем ногу слева
my_turtle.forward(200)
draw_leg()            # Рисуем ногу справа
my_turtle.left(180)
my_turtle.forward(200)
draw_body()           # Рисуем тело
draw_neck()           # Рисуем шею
draw_head()           # Рисуем голову
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(400)
my_turtle.left(90)
draw_ear()            # Рисуем ухо слева
my_turtle.forward(50)
draw_ear()            # Рисуем ухо справа

# Завершение рисования
my_turtle.screen.exitonclick()
