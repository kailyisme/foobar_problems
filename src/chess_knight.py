def append_seven(a_list: list):
    last_num = -1
    if a_list != []:
        last_num = a_list[-1][-1]
    new_list = [i for i in range(last_num + 1, last_num + 9)]
    a_list.append(new_list)


chess_table = []
append_seven(chess_table)
while chess_table[-1][-1] < 63:
    append_seven(chess_table)

# for y in chess_table:
#     line = ""
#     for x in y:
#         if x < 10:
#             line += f"0{x} "
#         else:
#             line += f"{x} "
#     print(line)

def poss_moves(from_point: int, table=chess_table):
    possible_moves = [
        [-2, -1],
        [-2, 1],
        [-1, 2],
        [1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
        [-1, -2],
    ]
    start_x, start_y = 0, 0
    for y_index, a_list in enumerate(table):
        to_break = False
        for x_index, num in enumerate(a_list):
            if num == from_point:
                start_x = x_index
                start_y = y_index
                to_break = True
                break
        if to_break == True:
            break
    moves = []
    for y, x in possible_moves:
        if (start_y + y) in range(len(table)) and (start_x + x) in range(len(table[(start_y + y)])):
            moves.append(table[start_y + y][start_x + x])
    return moves

def solver(starting_point: int, end_point: int, table=chess_table):
    if starting_point == end_point:
        return 0
    list_pos = {starting_point,}
    amount_moves = 0
    all_moves = {}
    while True:
        new_pos = []
        for pos in list_pos:
            moves_for_pos = poss_moves(pos, table)
            new_pos.extend(moves_for_pos)
            all_moves[f"{amount_moves},{pos}"] = moves_for_pos
        amount_moves += 1
        if end_point in new_pos:
            last_pos = end_point
            path = [end_point]
            for i in range(amount_moves):
                last_step = amount_moves - i -1
                for key in all_moves:
                    if int(key.split(",")[0]) == last_step and last_pos in all_moves[key]:
                        last_pos = int(key.split(",")[1])
                        path.append(last_pos)
                        break
            path = path[::-1]
            return amount_moves, path
        new_pos = [i for i in new_pos if i not in all_moves.keys()]
        list_pos = set(new_pos)

amount_of_steps, path = solver(0,1)
print(f"{amount_of_steps} steps from position {path[0]} to {path[-1]}")
for y in chess_table:
    line = ""
    for x in y:
        if x in path:
            line += f"0{path.index(x)} "
        else:
            line += f"__ "
    print(line)
amount_of_steps, path = solver(19,36)
print(f"{amount_of_steps} steps from position {path[0]} to {path[-1]}")
for y in chess_table:
    line = ""
    for x in y:
        if x in path:
            line += f"0{path.index(x)} "
        else:
            line += f"__ "
    print(line)
amount_of_steps, path = solver(0,63)
print(f"{amount_of_steps} steps from position {path[0]} to {path[-1]}")
for y in chess_table:
    line = ""
    for x in y:
        if x in path:
            line += f"0{path.index(x)} "
        else:
            line += f"__ "
    print(line)