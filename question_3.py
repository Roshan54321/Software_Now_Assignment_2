import turtle

# Recursive function to draw one edge with outward-pointing triangles
def draw_spiky_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_spiky_edge(t, length, depth - 1)
        t.right(60)  # Flip direction for outward spike
        draw_spiky_edge(t, length, depth - 1)
        t.left(120)
        draw_spiky_edge(t, length, depth - 1)
        t.right(60)
        draw_spiky_edge(t, length, depth - 1)

# Function to draw the full polygon with recursive edges
def draw_recursive_polygon(sides, length, depth):
    angle = 360 / sides
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()
    t.goto(-length / 2, length / 2)  # Center the drawing
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

# Run the program
main()