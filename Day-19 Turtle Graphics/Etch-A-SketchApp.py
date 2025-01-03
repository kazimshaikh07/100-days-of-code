from turtle import Turtle, Screen
yim = Turtle()
screen = Screen()

def yim_forward():
    yim.forward(10)
def yim_backward():
    yim.backward(10)
def yim_clockwise():
    yim.right(10)
def yim_anticlockwise():
    yim.left(10)
def yin_clear():
    yim.clear()
    yim.penup()
    yim.home()
    yim.pendown()
screen.listen()
screen.onkey(key="w",fun=yim_forward)
screen.onkey(key="s",fun=yim_backward)
screen.onkey(fun=yim_clockwise, key="d")
screen.onkey(fun=yim_anticlockwise, key="a")
screen.onkey(fun=yin_clear, key="c")
print(screen.exitonclick())