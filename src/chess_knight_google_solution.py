def solution(src, dest):
    table = [[i for i in range(8)],]
    while table[-1][-1] < 63:
        last_num = table[-1][-1]
        new_list = [i for i in range(last_num + 1, last_num + 9)]
        table.append(new_list)
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
    amount_moves = 0
    if src == dest:
        return amount_moves
    list_pos = {src,}
    while True:
        new_pos = []
        for pos in list_pos:
            start_x, start_y = 0, 0
            for y_index, a_list in enumerate(table):
                to_break = False
                for x_index, num in enumerate(a_list):
                    if num == pos:
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
            new_pos.extend(moves)
        amount_moves += 1
        if dest in new_pos:
            return amount_moves
        list_pos = set(new_pos)
