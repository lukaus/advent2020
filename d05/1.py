import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = -1
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)

rows = 128
cols = 8
for line in lines:
    row_bounds = [0, rows]
    col_bounds = [0, cols]
    for char in line:
        if char == "F":
            # front half of bounds
            row_bounds[1] -= int((row_bounds[1] - row_bounds[0]) / 2)

        elif char == "B":
            # back half of bounds
            row_bounds[0] += int((row_bounds[1] - row_bounds[0]) / 2)

        elif char == "L":
            col_bounds[1] -= int((col_bounds[1] - col_bounds[0]) / 2)

        elif char == "R":
            col_bounds[0] += int((col_bounds[1] - col_bounds[0]) / 2)
    seat_id = row_bounds[0] * 8 + col_bounds[0] 
    if seat_id > result:
        result = seat_id



print(result)


