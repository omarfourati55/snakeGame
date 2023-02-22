from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
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
        self.score = 0
        self.refresh_score()

    def increse_score(self):
        self.score += 1
        self.refresh_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
