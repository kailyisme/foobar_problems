def solution(x, y):
    working_space_matrix = [[1]]
    while True:
        if len(working_space_matrix) >= x:
            if len(working_space_matrix[x-1]) >= y:
                return str(working_space_matrix[x-1][y-1])
        last_working_space = working_space_matrix[-1][-1]
        for line in working_space_matrix:
            last_working_space += 1
            line.append(last_working_space)
        last_working_space += 1
        working_space_matrix.append([last_working_space])

assert solution(3,2) == "9"
assert solution(5,10) == "96"
