from turtle import Turtle

def make_polygon(t, no_of_sides, length, angle, rec_depth): 
    if no_of_sides <= 0:
        return
    make_edge(t, length, rec_depth)
    t.left(angle)
    make_polygon(t, no_of_sides - 1, length, angle, rec_depth)

def make_edge(t, length, rec_depth):
    if rec_depth < 1:
        t.forward(length)
        return
    else:
        length /= 3 # we divide the line into 3 equal segments
        # for first segment
        make_edge(t, length, rec_depth - 1)
        # for second segment - first part
        t.left(60)
        make_edge(t, length, rec_depth - 1)
        # for second segment - second part
        t.right(120)
        make_edge(t, length, rec_depth - 1)
        # for third segment
        t.left(60)
        make_edge(t, length, rec_depth - 1)

def main():
    try:
        no_of_sides = int(input("Enter the number of sides of the polygon: "))
        length = float(input("Enter the length of each side: "))
        rec_depth = float(input("Enter the recursion depth: "))

        t = Turtle()
        t.screen.title('Geometric Pattern - Polygon')
        ext_angle = 360 / no_of_sides

        # we are drawing to the upper side, so we always use left turn
        make_polygon(t, no_of_sides, length, ext_angle, rec_depth)
        t.screen.mainloop()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()