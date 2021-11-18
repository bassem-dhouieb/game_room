import turtle
from turtle import Turtle

FONT = ('Arial', 20, 'normal')
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score: {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over. ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def difficulty(self):
        choice = turtle.textinput("difficulty", "easy,medium,hard").lower()
        if choice == "easy":
            return 0.8
        elif choice == "medium":
            return 0.1
        else:
            return 0.05
