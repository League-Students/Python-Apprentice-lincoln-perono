import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
tina.speed(0)
def fractal_triangle(size,depth):
    if depth == 0:
        for i in range(4):
            tina.forward(size)
            tina.left(90)
    else:
        for i in range(4):
            fractal_triangle(size/2,depth-1)
            tina.forward(size)
            tina.left(90)
            
fractal_triangle(200,10)

turtle.exitonclick()