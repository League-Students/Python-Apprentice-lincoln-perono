import turtle

tina = turtle.Turtle()

screen=turtle.Screen()
screen.setup(500,500)

cam_colors = ["red","black","white","blue","green"]

def open_cam1():
    print("cam_1 open")
    screen.bgcolor(cam_colors[0])
def open_cam2():
    print("cam_2 open")
    screen.bgcolor(cam_colors[1])
def open_cam3():
    print("cam_3 open")
    screen.bgcolor(cam_colors[2])
def open_cam4():
    print("cam_4 open")
    screen.bgcolor(cam_colors[3])
def open_cam5():
    print("cam_5 open")
    screen.bgcolor(cam_colors[4])
def exit_cam():
    print("cam_5 open")
    screen.bgcolor(cam_colors[4])


screen.listen()
screen.onkey(open_cam1, "1")
screen.onkey(open_cam2, "2") 
screen.onkey(open_cam3, "3")
screen.onkey(open_cam4, "4")
screen.onkey(open_cam5, "5")
            
turtle.exitonclick()