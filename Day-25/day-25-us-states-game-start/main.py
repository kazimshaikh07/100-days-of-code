import turtle
import pandas
from numpy.ma.core import left_shift

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

screen = turtle.Screen()
screen.title("US State game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

"""# to get x and y coordinate from the map
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
"""
guessed_state = []

while len(guessed_state)<50:

    answer_state = screen.textinput(title=f"Guessed {len(guessed_state)}/50",
                                    prompt="What's is another state name!").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_state if state!=guessed_state]
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("State_to_learn.csv")
        break
    if answer_state in all_state:
        t =turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(x = state_data.x.item(), y = state_data.y.item())
        t.write(answer_state)
        guessed_state.append(answer_state)


# turtle.mainloop()
# screen.exitonclick()