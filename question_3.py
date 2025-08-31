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