def new_level(score, level):
    # global time_delay
    # global game_mode
    
    if score % 60 == 0:
        level += 1
        # time_delay -= 0.01

        if level == 10:
            # game_mode = 'win'
            print("\n10")

    return level


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
            for copy_y in range(curr_y, 0, -1):
                for copy_x in range(0, 12, 1):
                    field[copy_y][copy_x] = field[copy_y - 1][copy_x]
