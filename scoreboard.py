from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(align=ALIGNMENT, font=FONT, arg=f"Score: {self.score} High Score: {self.highscore}")

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.refresh_score()

    def increse_score(self):
        self.score += 1
        self.refresh_score()

