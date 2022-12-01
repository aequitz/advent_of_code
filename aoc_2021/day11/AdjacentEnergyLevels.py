'''
Determine flashes that occur over a given range (step 1 consists of 100 steps).
For each step, an octopus' energy level increases by 1. A flash occurs when an
octupus' energy level is greater than 9. A flash causes all adjacent octopi to
increase an additional energy level. If they are subsequently greater than 9,
they also flash. Once the energy level is greater than 9, that octupus resets to 0.

Austin Equitz
austin.equitz@gmail.com
'''

def adjacentArrayPoints(input_array: list, point_coord: list, get_diag_points=True) -> list:
    adj_coords = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    adj_idxs = []

    if get_diag_points:
        adj_coords += [-1, -1], [1, 1], [-1, 1], [1, -1]

    for coord in adj_coords:
        adj_idx = [a + b for a,b in zip(point_coord, coord)]

        not_negative = all(i >= 0 for i in adj_idx)
        not_exceed_row = (adj_idx[0] < len(input_array))
        not_exceed_col = (adj_idx[1] < len(input_array[0]))

        if all([not_negative, not_exceed_row, not_exceed_col]):
            adj_idxs.append(adj_idx)


    return adj_idxs


def print2DArray(array_in: list):
    for row in array_in:
        print(row)

def findFlashPoints(array_in: list, threshold: int) -> list:
    flash_points = []

    for row_idx,row in enumerate(array_in):
        for col_idx,val in enumerate(row):
            if val > threshold: flash_points.append([row_idx, col_idx])

    return flash_points


if __name__ == '__main__':
    with open('OctopusGrid.txt', 'r') as fin: octo_grid = [list(map(int,n)) for n in fin.read().splitlines()]

    print2DArray(octo_grid)
    total_flash_points = 0
    sync_flash_steps = []

    for i in range(400):
       
        octo_grid = [[val + 1 for val in row] for row in octo_grid]

        flash_points = findFlashPoints(octo_grid, 9)
        next_flash_points = flash_points

        while next_flash_points:
            
            for coordinate in next_flash_points:
                adj_points = adjacentArrayPoints(octo_grid, coordinate)

                for adj_point in adj_points:
                    row,col = map(int, adj_point)
                    octo_grid[row][col] += 1

            next_flash_points = [val for val in findFlashPoints(octo_grid, 9) if val not in flash_points]
            flash_points += next_flash_points

        total_flash_points += len(flash_points)
        octo_grid = [[val if val < 10 else 0 for val in row] for row in octo_grid]

        if all(x == 0 for row in octo_grid for x in row): sync_flash_steps.append(i + 1)
        
    print()
    print2DArray(octo_grid)
    print(total_flash_points)
    print(sync_flash_steps)
