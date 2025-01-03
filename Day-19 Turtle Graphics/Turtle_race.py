from turtle import Turtle,Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? enter a color")
print(user_bet)
color = ["red","green","purple","orange","yellow"]
y_position = [-80,-40,0,40,80]
all_turtles =[]

for turtle_index in range(0,5):
    new_turtle =Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    race_is_on =True
while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won, {winning_color} turtle win")
            else:
                print(f"you loss,{winning_color} turtle is winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# tim =Turtle(shape="turtle")
# tim.color(random.choice(color))
# tim.penup()
# tim.goto(x=-230,y=40)
# rim =Turtle(shape="turtle")
# rim.color(random.choice(color))
# rim.penup()
# rim.goto(x=-230,y=-40)
# kim =Turtle(shape="turtle")
# kim.color(random.choice(color))
# kim.penup()
# kim.goto(x=-230,y=80)
# yim =Turtle(shape="turtle")
# yim.color(random.choice(color))
# yim.penup()
# yim.goto(x=-230,y=-80)
screen.exitonclick()