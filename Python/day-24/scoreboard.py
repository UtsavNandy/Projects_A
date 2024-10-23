from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day-24/data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} high Score: {self.highscore}", align='center', font=("Courier", 20, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_score()

    def resetsb(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()



