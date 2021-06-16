import random

# Block shapes
square = [[1, 1],
          [1, 1]]

HOR_line = [[1, 1, 1, 1]]

VER_line = [[1],
            [1],
            [1],
            [1]]

LEFT_L = [[1, 0, 0, 0],
          [1, 1, 1, 1]]

RIGHT_L = [[0, 0, 0, 1],
           [1, 1, 1, 1]]

LEFT_S = [[1, 1, 0],
          [0, 1, 1]]

RIGHT_S = [[0, 1, 1],
           [1, 1, 0]]

T = [[0, 1, 0],
     [1, 1, 1]]


class Block:
    def __init__(self):
        self.x = random.randint(4, 6)
        self.y = 0
        self.color = random.randint(1, 7)

        shapes = [square, HOR_line, VER_line, LEFT_L, RIGHT_L, LEFT_S, RIGHT_S, T]

        # Random choice of shape
        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def move_left(self, field):
        # checks if x is bigger than 0 and if the position is free
        if self.x > 0 and field[self.y][self.x - self.width] == 0:
            self.delete_block(field)
            self.x -= 1

    def move_right(self, field):
        if self.x < (12 - self.width) and field[self.y][self.x + self.width] == 0:
            self.delete_block(field)
            self.x += 1

    def delete_block(self, field):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    field[self.y + y][self.x + x] = 0

    def rotate_block(self, field):
        # Delete shape
        self.delete_block(field)
        # New shape
        new_shape = []
        # Replace the row with the column and the column with the row
        for x in range(self.width):
            row = []
            for y in range(self.height - 1, -1, -1):
                row.append(self.shape[y][x])
            new_shape.append(row)

        # Checks if the new shape is going to be outside of the field
        if self.x + len(new_shape[0]) < len(field[0]):
            self.shape = new_shape
            # After the shape is changed its height and width must be changed too
            self.width = len(self.shape[0])
            self.height = len(self.shape)

    def draw_block(self, field):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    field[self.y + y][self.x + x] = self.color

    def collision(self, field):
        for x in range(self.width):
            print(self.height)
            print(self.x)
            print(x)
            print(self.y)
            print("=" * 50)
            # time.sleep(1)
            if self.shape[self.height - 1][x] == 1:
                if self.y + self.height > 23:
                    return False

                elif self.x + x > 11:
                    return False

                elif field[self.y + self.height][self.x + x] != 0:
                    return False

        return True
