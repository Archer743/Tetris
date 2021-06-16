import time

from block import *
from play import *
from score import *
from level import *

sound = 1
# sound = 1 => plays Tetris' theme
# sound = -1 => plays only block's sounds (if you are in the game)
# sound = 2 => stops every sound except the winning, losing, and clicking sounds
oncePlayed = True

# 0.05
time_delay = 0.1
game_mode = 'screen'
# every mode
# 'screen' => menu
# 'quit' => to get out of the game
# 'game' => start a game
# 'lose' => you have lost
# 'win' => you have won


#             y    x
# Game field 24 x 12
field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# __POINTS AND LEVEL__
if fileCheck("best_Score.txt"):
    info = (open("best_Score.txt", "r").read()).split('\n')
    best_level = int(info[0])
    best_points = int(info[1])
    wins = int(info[2])
    losses = int(info[3])


def save_stats(fileName, points, level, wins, losses):
    # Save the changes
    f = open(fileName, "w")

    f.write(str(level))
    f.write("\n")
    f.write(str(points))
    f.write("\n")
    f.write(str(wins))
    f.write("\n")
    f.write(str(losses))

    f.close()


# Part from the music
def playRepWithBut(fileName, number):
    if fileCheck(fileName):
        global sound
        sound = number
        if sound == 1:
            winsound.PlaySound(fileName, winsound.SND_ASYNC | winsound.SND_LOOP)
        else:
            winsound.PlaySound(None, winsound.SND_ALIAS)


class Button(turtle.Turtle):
    def __init__(self, Button_x, Button_y, ButtonLength, ButtonWidth, window, place, destination):
        turtle.Turtle.__init__(self)
        self.x = Button_x
        self.y = Button_y
        self.len = ButtonLength
        self.width = ButtonWidth
        self.win = window
        self.place = place
        self.dest = destination
        self.hideturtle()

    def button_click(self, x, y):
        global game_mode
        global field
        global best_points
        global best_level

        if self.place == game_mode:
            if self.x <= x <= self.x + self.len:
                if self.y <= y <= self.y + self.width:
                    print('Clicked')
                    play("click3.wav")
                    if self.dest == 'quit':
                        # Closes the window
                        time.sleep(0.3)
                        if level.level > best_level:
                            best_level = level.level

                        if score.score > best_points:
                            best_points = score.score

                        save_stats("best_Score.txt", best_points, best_level, wins, losses)
                        self.win.bye()
                    game_mode = self.dest

    def draw_button(self, color, message="Click Me"):
        self.fillcolor(color)
        self.penup()
        self.begin_fill()
        self.goto(self.x, self.y)
        self.goto(self.x + self.len, self.y)
        self.goto(self.x + self.len, self.y + self.width)
        self.goto(self.x, self.y + self.width)
        self.goto(self.x, self.y)
        self.end_fill()
        self.goto(self.x + 40, self.y + 25)
        self.write(message, font=('Arial', 15, 'normal'))

        # Get mouse cursor position in window
        # canvas = turtle.getcanvas()
        # x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
        # print(x, self.x, self.x + self.len, y, self.y, self.y + self.width)
        # self.button_click(x, y)


# New Level
def new_level(score, level):
    global time_delay
    global game_mode

    if score % 60 == 0:
        level += 1
        time_delay -= 0.01

        if level == 10:
            game_mode = 'win'

    return level


# Colors
Colors = ["brown", "red", "blue", "lightblue", "darkgreen", "orange", "purple", "yellow"]


# Drawing of the field
# stamp() => leaves a trail of pen's color
def draw_field(pen, field):
    pen.clear()
    left = -107
    top = 240
    for y in range(len(field)):
        for x in range(len(field[0])):
            W_x = left + (x * 20)
            W_y = top - (y * 20)

            pen.goto(W_x, W_y)
            pen.color(Colors[field[y][x]])
            pen.stamp()


# Checks if any row is full
def check_field(field):
    curr_y = 23
    while curr_y > 0:
        isFull = True
        for x in range(0, 12, 1):
            if field[curr_y][x] == 0:
                isFull = False
                curr_y -= 1
                break

        if isFull:
            score.change_score(20)
            level.level = new_level(score.score, level.level)
            # Audio
            if sound != 1 and sound != 2:
                play("line.wav")
            for copy_y in range(curr_y, 0, -1):
                for copy_x in range(0, 12, 1):
                    field[copy_y][copy_x] = field[copy_y - 1][copy_x]


# ______SET UP______
# Creates screen for the game
screen = turtle.Screen()
screen.title("TETRIS")
screen.bgcolor("Chocolate")
screen.setup(width=600, height=700)

# Using turtle object to draw the game
# speed(0) => everything will be drawn with max speed
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

# place = where the button will be used
# destination = where the button will take you away

Button1 = Button(-70, -50, 150, 70, screen, 'screen', 'game')
# Button1.draw_button(pen, 'red', "  PLAY  ")
Button2 = Button(-70, -150, 150, 70, screen, 'screen', 'quit')

Button3 = Button(-270, 260, 150, 70, screen, 'game', 'quit')

# Stops every update
screen.tracer(0)

# Create the first block
block = Block()
# Create and draw score
score = Score()
# Create and draw level
level = Level()

# Movement
# Screen will look for pressing this buttons
screen.listen()
screen.onkeypress(lambda: block.move_left(field), "Left")
screen.onkeypress(lambda: block.move_right(field), "Right")

screen.onkeypress(lambda: block.move_left(field), "a")
screen.onkeypress(lambda: block.move_right(field), "d")

# Rotation
screen.onkeypress(lambda: block.rotate_block(field), "space")

# Audio Control
# Play
screen.onkeypress(lambda: playRepWithBut("Tetris_Theme.wav", 1), "o")
screen.onkeypress(lambda: playRepWithBut("Tetris_Theme.wav", -1), "p")
screen.onkeypress(lambda: playRepWithBut("Tetris_Theme.wav", 2), "l")

# 1 = left button
# 2 = middle button
# 3 = right button
screen.onscreenclick(Button1.button_click, 1)
screen.onscreenclick(Button2.button_click, 3)
screen.onscreenclick(Button3.button_click, 2)

playRep("Tetris_Theme.wav")

# Game Loop
while True:
    # Everything will be updated by every iteration of the game loop
    # Makes the gameplay smoother
    screen.update()

    if game_mode == 'game':

        if oncePlayed:
            sound = -1
            oncePlayed = False

        # Draw the field
        draw_field(pen, field)

        if block.y == 0 and field[block.y + block.height][block.x] != 0:
            play("gameover.wav")
            game_mode = 'lose'

            if level.level > best_level:
                best_level = level.level

            if score.score > best_points:
                best_points = score.score

            save_stats("best_Score.txt", best_points, best_level, wins, losses)

        # If the block's y is at the bottom of the field
        elif block.y == 23 - block.height + 1:
            block = Block()
            # Audio
            if sound != 1 and sound != 2:
                play("dead.wav")
            # Is any row full
            check_field(field)

        elif block.collision(field):
            # Delete the block
            block.delete_block(field)
            # Moving the block down by 1
            block.y += 1
            # Drawing the block again
            block.draw_block(field)

        else:
            block = Block()
            # Audio
            if sound != 1 and sound != 2:
                play("dead.wav")
            # Is any row full
            check_field(field)

        if game_mode == 'game':
            draw_field(pen, field)
            # Updates the score
            score.update_score()
            # Updates the level
            level.update_level()
            # Button is drawn
            pen.color("black")
            Button3.draw_button('red', "  QUIT  ")

        else:
            screen.clear()
            screen.bgcolor("Chocolate")

    elif game_mode == 'screen':
        pen.color("black")
        pen.goto(-150, 150)
        pen.write("TETRIS", font=('Segoe Print', 60, 'normal'))

        Button1.draw_button('red', "  PLAY  ")
        Button2.draw_button('red', "  QUIT  ")

        pen.color("black")
        pen.goto(-70, -200)
        pen.write(f"BEST LEVEL: {best_level}", font=('Arial', 15, 'normal'))

        pen.goto(-70, -240)
        pen.write(f"BEST POINTS: {best_points}", font=('Arial', 15, 'normal'))

        pen.goto(-70, -280)
        pen.write(f"WINS: {wins}", font=('Arial', 15, 'normal'))

        pen.goto(-70, -320)
        pen.write(f"LOSSES: {losses}", font=('Arial', 15, 'normal'))

    elif game_mode == 'win':
        pen.color("black")
        pen.goto(-200, 120)
        pen.write("YOU WIN!", font=('Segoe Print', 60, 'normal'))

        wins += 1
        best_level = level.level
        best_points = score.score

        save_stats("best_Score.txt", best_points, best_level, wins, losses)

        play("Ta_Da.wav")
        time.sleep(2)
        play("Fire_Crackers.wav")

        time.sleep(3)
        screen.bye()

    elif game_mode == 'lose':

        pen.color("black")
        pen.goto(-200, 120)
        pen.write("YOU LOST!", font=('Segoe Print', 60, 'normal'))

        losses += 1
        save_stats("best_Score.txt", best_points, best_level, wins, losses)

        play("loss.wav")

        time.sleep(3)
        screen.bye()

    # Makes the gameplay smoother
    time.sleep(time_delay)
