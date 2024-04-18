import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=800, height=600)

# Create turtles
colors = ["red", "blue", "green", "orange", "purple"]
turtles = []
for i, color in enumerate(colors):
    turtles.append(turtle.Turtle())
    turtles[i].shape("turtle")
    turtles[i].color(color)
    turtles[i].penup()
    turtles[i].goto(-300, 100 - i * 50)

# Race function
def race():
    winner = False
    while not winner:
        for turtle in turtles:
            distance = random.randint(1, 20)
            turtle.forward(distance)
            if turtle.xcor() >= 300:
                winner = True
                winning_color = turtle.color()
                break

    screen.textinput("Winner", f"The {winning_color[0]} turtle wins!")

# Start the race
race()

# Keep the window open
screen.mainloop()
