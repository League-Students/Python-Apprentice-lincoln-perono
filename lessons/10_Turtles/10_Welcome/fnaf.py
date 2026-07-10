import turtle
import time

tina = turtle.Turtle()
tina.shape("turtle")
tina_path = [1,2,4,5]
tina_progress = 0


screen=turtle.Screen()
screen.setup(500,500)

cam_colors = ["red","gray","white","blue","green"]


def move_tina():
    global tina_progress
    tina_progress += 1
    show_animatronics()
    screen.ontimer(move_tina,2000)
def show_animatronics():
    if(cam_num == tina_path[tina_progress]):
        tina.showturtle()
    else:
        tina.hideturtle()
def open_cam1():
    global tina_progress
    tina_progress += 1
    print("cam_1 open")
    screen.bgcolor(cam_colors[0])
    show_animatronics()
def open_cam2():
    global tina_progress
    tina_progress += 2
    print("cam_2 open")
    screen.bgcolor(cam_colors[1])
    show_animatronics()
def open_cam3():
    global tina_progress
    tina_progress += 3
    print("cam_3 open")
    screen.bgcolor(cam_colors[2])
    show_animatronics()
def open_cam4():
    global tina_progress
    tina_progress += 4
    print("cam_4 open")
    screen.bgcolor(cam_colors[3])
    show_animatronics()
def open_cam5():
    global tina_progress
    tina_progress += 5
    print("cam_5 open")
    screen.bgcolor(cam_colors[4])
    show_animatronics()
def exit_cam():
    print("cam exited")
    screen.bgcolor("yellow")
    show_animatronics()

exit_cam()

screen.listen()
screen.onkey(open_cam1, "1")
screen.onkey(open_cam2, "2") 
screen.onkey(open_cam3, "3")
screen.onkey(open_cam4, "4")
screen.onkey(open_cam5, "5")
screen.onkey(exit_cam, "0")

screen.ontimer(move_tina,2000)

turtle.exitonclick()