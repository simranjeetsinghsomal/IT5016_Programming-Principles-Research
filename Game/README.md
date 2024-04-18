# Turtle Race Game

## Introduction
This Python program implements a simple turtle race game using the turtle module. In this game, turtles of different colors race across the screen, and the first turtle to reach the finish line wins the race.

## Programming Principles and Concepts
### 1. Object-Oriented Programming (OOP)
- The turtle race game demonstrates the use of object-oriented programming principles. Here's how it applies:
- Classes: The Turtle class from the turtle module is used to create turtle objects. Each turtle object represents a participant in the race.
- Encapsulation: Each turtle object encapsulates its state (position, color, etc.) and behavior (moving forward) within its instance methods.
- Inheritance: While not explicitly shown in this example, the Turtle class inherits properties and methods from its parent classes, such as RawTurtle and ScrolledCanvas.
### 2. Iteration (Looping)
- The game utilizes loops to control the flow of the race:
- While Loop: The race continues until one of the turtles reaches the finish line. This is achieved using a while loop that checks for the condition of a winner.
- For Loop: Inside the while loop, a for loop is used to iterate over each turtle, simulating their movement forward.
### 3. Conditionals
- Conditional statements are used to determine the winner of the race:
- If Statement: Within the for loop, an if statement checks if a turtle has crossed the finish line (reached xcor() >= 300). If so, that turtle is declared the winner, and the race ends.
### 4. Randomization
- The game introduces randomness to simulate the unpredictable nature of a race:
- Random Module: The random module is used to generate random distances for turtle movement (random.randint(1, 20)). This adds variability to the race outcome.
