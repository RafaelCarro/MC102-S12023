def print_room():
    '''Function that prints the current state of the room.
    '''
    for i in range(size_y):
        for j in range(size_x):
            if j != size_x - 1:
                print(room[i][j], end = " ")
            else:
                print(room[i][j], end = "")
        print()
    print()

def get_room_matrix(size_y):
    '''Function that gets the iniital state of the room.
    '''
    room = []
    for i in range(size_y):
        room.append(input().split())
    return room

def move_right():
    '''Moves the robot one space to the right.
    '''
    room[pos["y"]][pos["x"]] = "."
    pos["x"] += 1
    room[pos["y"]][pos["x"]] = "r"
    print_room()

def move_left():
    '''Moves the robot one space to the left.
    '''
    room[pos["y"]][pos["x"]] = "."
    pos["x"] -= 1
    room[pos["y"]][pos["x"]] = "r"
    print_room()

def move_up():
    '''Moves the robot up one space.
    '''
    room[pos["y"]][pos["x"]] = "."
    pos["y"] -= 1
    room[pos["y"]][pos["x"]] = "r"
    print_room()

def move_down():
    '''Moves the robot down one space.
    '''
    room[pos["y"]][pos["x"]] = "."
    pos["y"] += 1
    room[pos["y"]][pos["x"]] = "r"
    print_room()

def check_vicinity():
    '''Checks the vicinity of the robot for trash.
    '''
    if (pos["x"] > 0 and room[pos["y"]][pos["x"] - 1] == "o"):
        return 1
    elif (pos["y"] > 0 and room[pos["y"] - 1][pos["x"]] == "o"):
        return 2
    elif (pos["x"] + 1 < size_x and room[pos["y"]][pos["x"] + 1] == "o"):
        return 3
    elif (pos["y"] + 1 < size_y and room[pos["y"] + 1][pos["x"]] == "o"):
        return 4
    else:
        return 0

def scanning_mode():
    '''Scanning mode that moves if there aren't any trash out of the way.
    '''
    vicinity = check_vicinity()
    if vicinity == 0:
        if pos["y"] % 2 == 0:
            if pos["x"] + 1 == size_x and pos["y"] + 1 == size_y:
                return 0
            elif pos["x"] + 1 == size_x:
                move_down()
            else:
                move_right()
        else:
            if pos["x"] == 0 and pos["y"] + 1 == size_y:
                for i in range(size_x):
                    move_right()
            elif pos["x"] == 0:
                move_down()
            else:
                move_left()
        scanning_mode()
    else:
        if pos["y"] % 2 == 0:
            if vicinity == 3:
                move_right()
                scanning_mode()
            elif vicinity == 4 and pos["x"] + 1 == size_x:
                move_down()
                scanning_mode()
            else:
                cleaning_mode(in_path, last_pos)
        else:
            if vicinity == 1:
                move_left()
                scanning_mode()
            elif vicinity == 4 and pos["x"] == 0:
                move_down()
                scanning_mode()
            else:
                cleaning_mode(in_path, last_pos)
    return 0

def cleaning_mode(in_path, last_pos):
    '''Cleaning mode, if entered, goes cleaning all the trash that is connected,
    them returns to the original position.
    '''
    vicinity = check_vicinity()
    if in_path == 0:
        last_pos = pos.copy()
        in_path = 1
    if vicinity == 1:
        move_left()
    elif vicinity == 2:
        move_up()
    elif vicinity == 3:
        move_right()
    elif vicinity == 4:
        move_down()
    else:
        return_to_path(in_path, last_pos)
    vicinity = check_vicinity
    if vicinity == 0:
        return 0
    else:
        cleaning_mode(in_path, last_pos)

def return_to_path(in_path, last_pos):
    '''Returns the robot to the last position before the cleaning mode.
    '''
    global end_flag
    if pos["y"] % 2 == 0:
        if pos["x"] + 1 == size_x and pos["y"] + 1 == size_y:
            if end_flag == 1:
                end_flag = 0
            else:
                return 0
    else:
        if pos["x"] == 0 and pos["y"] + 1 == size_y:
            if end_flag == 1:
                end_flag = 0
            else:
                for i in range(size_x):
                    move_right()
                return 0
    while pos["x"] > last_pos["x"]:
        move_left()
        cleaning_mode(in_path, last_pos)
    while pos["x"] < last_pos["x"]:
        move_right()
        cleaning_mode(in_path, last_pos)
    while pos["y"] > last_pos["y"]:
        move_up()
        cleaning_mode(in_path, last_pos)
    while pos["y"] < last_pos["y"]:
        move_down()
        cleaning_mode(in_path, last_pos)
    in_path = 0
    scanning_mode()
    return 0

if __name__ == "__main__":
    size_y = int(input())
    room = get_room_matrix(size_y)
    size_x = len(room[0])
    pos = {"x": 0, "y": 0}
    last_pos = pos.copy()
    in_path = 0
    end_flag = 0
    if size_y % 2 == 1 and room[size_y - 1][size_x - 1] == "o":
        end_flag = 1
    elif size_y % 2 == 0 and room[size_y - 1][0] == "o":
        end_flag = 1
    print_room()
    scanning_mode()