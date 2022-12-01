'''
Find intersecting points given a list
of start/end points that form a line.

Austin Equitz
austin.equitz@gmail.com
'''

import numpy as np

if __name__ == '__main__':
    # Reads in text file as list[str]
    with open('InputPoints.txt', 'r') as fin: points_in = [n.strip() for n in fin.readlines()]

    # Create list(list(tuple)) for coordinates
    coords = []
    for idx,line in enumerate(points_in):
        coords = coords + [[eval(coord) for coord in line.split(" -> ")]]

    # Initialize grid
    max_coord = np.amax(coords)
    grid = np.zeros([max_coord+1, max_coord+1])

    # Create different line types
    horz_lines = [x for x in coords if x[0][1] == x[1][1]]
    vert_lines = [x for x in coords if x[0][0] == x[1][0]]
    diag_lines = [x for x in coords if x[0][1] != x[1][1] and x[0][0] != x[1][0]]

    # Draw horizontal lines
    for line in horz_lines:
        start_line = min(line)
        end_line = max(line)
        y = start_line[1]

        for x in range(start_line[0], end_line[0]+1):
            np.add.at(grid, (y, x), 1)

    # Draw vertical lines
    for line in vert_lines:
        start_line = min(line)
        end_line = max(line)
        x = start_line[0]

        for y in range(start_line[1], end_line[1]+1):
            np.add.at(grid, (y, x), 1)

    # Draw diagonal lines (comment out for part 1 only)
    for line in diag_lines:
        start_line = min(line)
        end_line = max(line)
        x = start_line[0]
        slope = (1 if start_line[1] < end_line[1] else -1)

        for idx,y in enumerate([item for item in range(start_line[1], end_line[1]+slope, slope)]):
            np.add.at(grid, (y, x+idx), 1)

    # Print results
    print(grid)
    print(len(grid[grid>=2]))