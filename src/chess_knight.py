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

for y in chess_table:
    line = ""
    for x in y:
        if x < 10:
            line += f"0{x} "
        else:
            line += f"{x} "
    print(line)

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
    while True:
        new_pos = []
        for pos in list_pos:
            new_pos.extend(poss_moves(pos, table))
        amount_moves += 1
        if end_point in new_pos:
            return amount_moves
        list_pos = set(new_pos)

print(solver(0,1))
print(solver(19,36))