
import turtle

# Recursive function to draw one edge with outward-pointing triangles
def draw_spiky_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_spiky_edge(t, length, depth - 1)
        t.right(60)
        draw_spiky_edge(t, length, depth - 1)
        t.left(120)
        draw_spiky_edge(t, length, depth - 1)
        t.right(60)
        draw_spiky_edge(t, length, depth - 1)

# Function to draw just one spiky segment (_\/_) when depth == 1
def draw_single_spike():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 0)
    t.pendown()

    segment = 100  # 300 / 3
    t.forward(segment)
    t.right(60)
    t.forward(segment)
    t.left(120)
    t.forward(segment)
    t.right(60)
    t.forward(segment)

    turtle.done()

# Function to draw the full polygon with recursive edges
def draw_recursive_polygon(sides, length, depth):
    t = turtle.Turtle()
    t.speed(0)

    if depth == 0:
        # Constant output: one straight line of length 300
        sides = 1
        length = 300
        t.penup()
        t.goto(-length / 2, 0)
        t.pendown()
        t.forward(length)

    elif depth == 1:
        # Special case: draw _\/_
        draw_single_spike()
        return

    else:
        angle = 360 / sides
        t.penup()
        t.goto(-length / 2, length / 2)
        t.pendown()
        for _ in range(sides):
            draw_spiky_edge(t, length, depth)
            t.right(angle)

    turtle.done()

# Main function to get user input and start drawing
def main():
    sides = int(input("Enter the number of sides: "))
    length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    draw_recursive_polygon(sides, length, depth)

main()
