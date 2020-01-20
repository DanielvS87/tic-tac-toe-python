# singles = []
# doubles = []
# triples = []
# throw_outs = []
#
# # fill up the lists with the possibilities
# for num in range(1, 22):
#     if num == 21:
#         singles.append(25)
#         doubles.append(50)
#     else:
#         singles.append(int(num))
#         doubles.append(2*int(num))
#         triples.append(3*int(num))
#
#
# def multi_nested_loop(matched_num, arr1, arr2, arr3=[]):
#     matches = []
#     for num1 in arr1:
#         for num2 in arr2:
#             # only when three arrays are given
#             if len(arr3) != 0:
#                 for num3 in arr3:
#                     total = num1 + num2 + num3
#                     if matched_num == total:
#                         order = f"{num1}, {num2}, {num3}"
#                         matches.append(order)
#             else:
#                 total = num1 + num2
#                 if matched_num == total:
#                     order = f"{num1}, {num2}"
#                     matches.append(order)
#     return matches
#
#
# def possible_outs():
#     points_left = int(input("How much point are left? "))
#     darts_remaining = int(input("How many darts are left? "))
#     possibilities = []
#     if points_left in doubles:
#         possibilities.append(points_left)
#     if darts_remaining == 2:
#         if points_left < 71 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, singles, doubles)
#         if points_left < 111 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, triples, doubles)
#             possibilities2 = multi_nested_loop(points_left, doubles, doubles)
#             for number in possibilities2:
#                 possibilities.append(number)
#     elif darts_remaining == 3:
#         if points_left < 91 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, singles, singles, doubles)
#         if points_left < 136 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, singles, triples, doubles)
#         if points_left < 171 and len(possibilities) == 0:
#             possibilities = multi_nested_loop(points_left, triples, triples, doubles)
#             possibilities2 = multi_nested_loop(points_left, triples, doubles, doubles)
#             for number in possibilities2:
#                 possibilities.append(number)
#     return possibilities
#
#
# list_outs = possible_outs()
# for option in list_outs:
#     print(option)
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
