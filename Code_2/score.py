import turtle


class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("black")
        self.goto(110, 300)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("SCORE: {}".format(self.score), False, align="left", font=("Arial", 24, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()
