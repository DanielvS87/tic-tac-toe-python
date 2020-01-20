winner_combinations = [[0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8],
                       [0, 3, 6],
                       [1, 4, 7],
                       [2, 5, 8],
                       [0, 4, 8],
                       [2, 4, 6]]


def winner_check(arr):
    winner = False
    for comb in winner_combinations:
        if arr[comb[0]] == arr[comb[1]] == arr[comb[2]] and arr[comb[0]] != " ":
            winner = True
    return winner


def tic_tac_toe():
    is_winner = False
    game_end = False
    cross_turn = True
    num_turn = 0
    filled_spots = []
    p = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    cross = "x"
    circle = "o"
    fields = {"ul": 0, "uc": 1, "ur": 2, "cl": 3, "cc": 4, "cr": 5, "ll": 6, "lc": 7, "lr": 8}
    board = f"{p[0]} | {p[1]} | {p[2]}\n- - - - -\n{p[3]} | {p[4]} | {p[5]}" \
            f"\n- - - - -\n{p[6]} | {p[7]} | {p[8]}"
    while not game_end and not is_winner:
        print(board)
        turn = cross_turn and "cross" or "circle"
        location = input(f"where you want to put a {turn}? ")
        if location in filled_spots:
            print("spot already filled, pick another one")
        else:
            filled_spots.append(location)
            p[fields[f"{location}"]] = cross_turn and cross or circle
            board = f"{p[0]} | {p[1]} | {p[2]}\n- - - - -\n{p[3]} | {p[4]} | {p[5]}" \
                f"\n- - - - -\n{p[6]} | {p[7]} | {p[8]}"
            is_winner = winner_check(p)
            num_turn = num_turn + 1
            if num_turn == 9:
                print(board, "\nno winner this time")
                game_end = True
            if is_winner:
                print(board)
                print(f"The Winner is {turn}")
        if cross_turn:

            cross_turn = False
        else:
            cross_turn = True


tic_tac_toe()
