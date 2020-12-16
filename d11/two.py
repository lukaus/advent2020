import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = 0
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)


def get_neighbors_count(row, col, board):
    live_count = 0

    c = col - 1
    r = row - 1
    while c >= 0 and r >= 0:
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        c -= 1
        r -= 1

    r = row - 1
    c = col
    while r >= 0:
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        r -= 1

    c = col + 1
    r = row - 1
    while c < len(board[r]) and r >= 0:
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        r -= 1
        c += 1

    c = col - 1
    r = row
    while c >= 0:
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        c -= 1

    c = col + 1
    r = row
    while c < len(board[r]):
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        c += 1

    c = col - 1
    r = row + 1
    while c >= 0 and r < len(board):
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        c -= 1
        r += 1

    r = row + 1
    c = col 
    while r < len(board): 
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        r += 1

    c = col + 1
    r = row + 1
    while r < len(board) and c < len(board[r]):
        if board[r][c] == "E":
            break
        elif board[r][c] == "#":
            live_count += 1
            break
        r += 1
        c += 1

    return live_count 



a_board = []
row = 0
for line in lines:
    a_board.append([])
    for tile in line:
        if tile == ".":
            a_board[row].append( ".")
        elif tile == "L":
            a_board[row].append("E")
    row += 1

b_board = []
for row in a_board:
    b_board.append(row.copy())

finished = False
while not finished:
    # Simulate a round
    for r in range(len(a_board)):
        for c in range(len(a_board[r])):
            # Skip floors
            if a_board[r][c] == ".":
                continue

            # Check the live neighbors
            live_count = get_neighbors_count(r, c, b_board)

            if b_board[r][c] == "E" and live_count == 0:
                a_board[r][c] = "#"
            elif b_board[r][c] == "#" and live_count >= 5:
                a_board[r][c] = "E"

    
    finished = True
    for r in range(len(a_board)):
        for c in range(len(a_board[r])):
            if b_board[r][c] != a_board[r][c]:
                finished = False
            b_board[r][c] = a_board[r][c]


for row in a_board:
    for tile in row:
        if tile == "#":
            result += 1
print(result)


