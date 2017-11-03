import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    i=1
    j=1
    for j in range(0,36):
        for i in range (0,4):
            brad.forward(50)
            brad.right(90)
        brad.right(10)

    window.exitonclick()

draw_square()
