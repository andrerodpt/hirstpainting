from color_extract import extract_colors_from_image
import random
from turtle import Turtle, Screen

NR_COLORS_TO_EXTRACT = 50
color_stack = extract_colors_from_image(NR_COLORS_TO_EXTRACT)

DOT_SIZE = 20
SPACING = 50
NR_DOTS_PER_ROW = 10
NR_DOTS_PER_COLUMN = 10

tim = Turtle(visible=False)
tim.speed('fastest')
tim.penup()
screen = Screen()
screen.colormode(255)

screen.setup(SPACING * (NR_DOTS_PER_ROW), SPACING * (NR_DOTS_PER_ROW))

x = -((SPACING * (NR_DOTS_PER_ROW - 1))/2)
y = -((SPACING * (NR_DOTS_PER_COLUMN - 1))/2)

for _ in range(NR_DOTS_PER_COLUMN):
    tim.setposition(x, y)
    for _ in range(NR_DOTS_PER_ROW):
        color = random.choice(color_stack)
        tim.dot(DOT_SIZE, color)
        tim.forward(SPACING)
    y += SPACING


screen.exitonclick()




