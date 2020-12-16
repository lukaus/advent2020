import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = 0
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)




def get_neighbors(row, col, max_rows, max_cols):
    neighbors = []

    if row-1 >= 0:
        neighbors.append([r-1, col])

        if col-1 >= 0:
            neighbors.append([r-1, col-1])

        if col+1 < max_cols:
            neighbors.append([r-1, col+1])


    if row+1 < max_rows:
        neighbors.append([r+1, col])
        if col-1 >= 0:
            neighbors.append([r+1, col-1])

        if col+1 < max_cols:
            neighbors.append([r+1, col+1])

    if col-1 >= 0:
        neighbors.append([row, col-1])

    if col+1 < max_cols:
        neighbors.append([row, col+1])

    return neighbors



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
            live_count = 0
            
            neighbors = get_neighbors(r, c, len(a_board), len(a_board[r]))
            for n in neighbors:
                if b_board[n[0]][n[1]] == "#":
                    live_count += 1

            #print(f"live: {live_count}")
            if b_board[r][c] == "E" and live_count == 0:
                a_board[r][c] = "#"
            elif b_board[r][c] == "#" and live_count >= 4:
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


