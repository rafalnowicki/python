import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()
tim.shape("turtle")
tim.color("orange")
screen.screensize(400, 400, "black")
tim.speed(2)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def line():
    for _ in range(0, 10):
        tim.penup()
        tim.forward(10)
        tim.pendown()
        tim.forward(10)


def shape(turn):
    tim.forward(100)
    tim.right(turn)


def drawing():
    def draw_shape(num_sides):
        for _ in range(num_sides):
            angle = 360 / num_sides
            tim.forward(100)
            tim.right(angle)

    for shape_side_n in range(3, 11):
        tim.color(random_color())
        draw_shape(shape_side_n)


def walk():
    tim.shape("classic")
    directions = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed("fastest")

    for _ in range(200):
        random_color()
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))


def spirograph():
    tim.shape("classic")
    tim.speed("fastest")
    def draw_spirograph(size_of_gap):
        for _ in range(int(360 / size_of_gap)):
            tim.color(random_color())
            tim.circle(100)
            tim.setheading(tim.heading() + size_of_gap)
    draw_spirograph(5)







spirograph()

screen.exitonclick()
