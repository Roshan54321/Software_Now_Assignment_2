import turtle
import math

def draw_koch_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_edge(t, length, depth - 1)
        t.left(60)
        draw_koch_edge(t, length, depth - 1)
        t.right(120)
        draw_koch_edge(t, length, depth - 1)
        t.left(60)
        draw_koch_edge(t, length, depth - 1)

def draw_recursive_polygon(sides, length, depth):
    angle = 360 / sides
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing

    for _ in range(sides):
        draw_koch_edge(t, length, depth)
        t.right(angle)

    turtle.done()