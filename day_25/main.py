from hashlib import new
import turtle
import pandas as pd

#Screen settings
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read CSV
data = pd.read_csv("50_states.csv")

# my solution
states = []
for i in range(len(data)):
    state = data.state[i]
    states.append(state)
    """or just states = data.states.to_list() :,)"""

guessed_states = []
while len(guessed_states)<50:
    # Answer Window
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state's name?").title()
    if answer_state == "Exit":
        # states to learn.csv
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        write_state = turtle.Turtle()
        write_state.hideturtle()
        write_state.penup()
        state_data = data[data.state == answer_state]
        write_state.goto(int(state_data.x), int(state_data.y))
        write_state.write(state_data.state.item())



