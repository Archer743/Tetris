import turtle


class Level(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("black")
        self.goto(-65, 300)
        self.level = 1

    def update_level(self):
        self.clear()
        self.write("Level: {}".format(self.level), False, align="left", font=("Arial", 24, "normal"))

    def change_level(self, level):
        self.level += level
        self.update_level()