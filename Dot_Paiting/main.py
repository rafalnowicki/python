# import colorgram
# colors = colorgram.extract('image.jpeg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append((new_color))
# print(rgb_colors)

color_list = [(142, 97, 19), (152, 168, 17), (222, 242, 41), (62, 26, 56), (149, 20, 91), (152, 150, 248), (95, 94, 7), (169, 41, 119), (31, 132, 63), (232, 154, 73), (191, 226, 14), (77, 38, 11), (130, 151, 227), (250, 232, 176), (35, 30, 69), (215, 56, 163), (59, 37, 135), (148, 32, 15), (48, 94, 155), (100, 87, 229), (204, 222, 251), (229, 118, 187), (58, 180, 66), (249, 199, 235), (247, 152, 208), (23, 101, 54), (222, 81, 55), (94, 205, 121), (193, 249, 222), (119, 239, 126)]


import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
