board1 = [' ' for x in range(10)]
board2 = [' ' for y in range(10)]
board3 = [' ' for z in range(10)]

Player1 = input("Player1 please enter your name: ")
Player2 = input("Player2 please enter your name: ")


def rules():
    print("""    1. There are 3 boards, each of 3 by 3 dimension.
    2. There will be only one variable to mark a move, which is "X".
    3. You are free to mark on any board at any position, until or unless it is occupied.
    4. If there is a configuration on a board which shows three Xs are line up either in rows, column or diagonals, the board will be consider dead.
    5. Dead board will not take part in the game ahead.
    6. One who kills the last board is the winner.""")


def insertLetter(letter, pos, bonum):
    if bonum == 1:
        board1[pos] = letter
    elif bonum == 2:
        board2[pos] = letter
    elif bonum == 3:
        board3[pos] = letter


def spaceIsFree(pos, bonum):
    if bonum == 1:
        return board1[pos] == " "
    elif bonum == 2:
        return board2[pos] == " "
    elif bonum == 3:
        return board3[pos] == " "


def printBoard(board1, board2, board3):
    print([board1[i] for i in range(1, 4)], [board2[i]
          for i in range(1, 4)], [board3[i] for i in range(1, 4)])
    print([board1[i] for i in range(4, 7)], [board2[i]
          for i in range(4, 7)], [board3[i] for i in range(4, 7)])
    print([board1[i] for i in range(7, 10)], [board2[i]
          for i in range(7, 10)], [board3[i] for i in range(7, 10)])
    bol_board1 = bool(isDead(1, "X"))
    bol_board2 = bool(isDead(2, "X"))
    bol_board3 = bool(isDead(3, "X"))
    print(
        str(" ") * 6 + "DEAD" * bol_board1 + str(" ") * 11 + "DEAD" * bol_board2 + str(" ") * 11 + "DEAD" * bol_board3)


def board_num():
    try:
        bonum = int(input("Please Enter the board number (1-3): "))
        if isDead(bonum, "X"):
            print("This board is dead. Select another board!")
            return board_num()
        elif 0 < bonum < 4:
            return bonum
        print("Number out of range!")
        return board_num()
    except:
        print("Invalid Input!")
        return board_num()


def isDead(bonum, le):
    if bonum == 1:
        bo = board1
    elif bonum == 2:
        bo = board2
    elif bonum == 3:
        bo = board3

    rows = (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
        bo[1] == le and bo[2] == le and bo[3] == le)
    columns = (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (
        bo[3] == le and bo[6] == le and bo[9] == le)
    diagonals = (bo[1] == le and bo[5] == le and bo[9] == le) or (
        bo[3] == le and bo[5] == le and bo[7] == le)

    return rows or columns or diagonals


def player1Move():
    while True:
        bonum = board_num()
        move = input(
            f"Please select a position to place an X (1-9) {Player1}: ")
        try:
            move = int(move)
            if 0 < move < 10 and 1 <= bonum <= 3:
                if not (isDead(bonum, le="X")):
                    if spaceIsFree(move, bonum):
                        insertLetter("X", move, bonum)
                        break
                    print("This space is occupied, select a free position")
                else:
                    print("This board is dead!")
            else:
                print("input number is out of range")
        except:
            print("Please give a number!")
    return bonum


def player2Move():
    while True:
        bonum = board_num()
        move = input(
            f"Please select a position to place an X (1-9) {Player2}: ")
        try:
            move = int(move)
            if 0 < move < 10 and 1 <= bonum <= 3:
                if not (isDead(bonum, le="X")):
                    if spaceIsFree(move, bonum):
                        insertLetter("X", move, bonum)
                        break
                    print("This space is occupied, select a free position")
                else:
                    print("This board is dead!")
            else:
                print("input number is out of range")
        except:
            print("Please give a number!")
    return bonum


def decision():
    intention = input("Do you want to play game?(Y/N): ")
    if intention.lower() in ["y", "n"]:
        return intention.lower()
    print("Invalid input!")
    return decision()


def main():
    steps = 0
    rules()
    if decision() == "y":
        import pandas as pd
        start = pd.Timestamp.now()
        printBoard(board1, board2, board3)
        count = 0
        while True:
            bonum = player1Move()
            printBoard(board1, board2, board3)
            steps += 1
            if (isDead(bonum, "X")):
                count += 1
            if count == 3:
                print(f"{Player1} wins")
                print(
                    f"{Player1} took {pd.Timestamp.now() - start} time and {steps} steps to win the game")
                break
            bonum = player2Move()
            printBoard(board1, board2, board3)
            steps += 1
            if (isDead(bonum, le="X")):
                count += 1
            if count == 3:
                print(f"{Player2} wins")
                print(
                    f"{Player2} took {pd.Timestamp.now() - start} time and {steps} steps to win the game")
                break
    else:
        print("Thanks You :)")


main()
