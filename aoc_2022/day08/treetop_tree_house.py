'''
Day 7: No Space Left On Device

Austin Equitz
austin.equitz@gmail.com
'''
import itertools

with open('tree_grid.txt', 'r') as fin: tree_input = fin.read().splitlines()

tree_grid = [[int(char) for char in line] for line in tree_input]

# Get stop indexes so outer border of trees is ignored
num_rows = len(tree_grid)
num_cols = len(tree_grid[0])
row_stop_idx = num_rows - 1
col_stop_idx = num_rows - 1

# Get index combinations to test around each tree
all_areas = list(itertools.permutations([-1, 0, 1], 2))
adj_tree_idxs = [(row,col) for row,col in all_areas if abs(row) != abs(col)]

# Calculate perimeter trees
perimeter_trees = num_rows * 2 + num_cols * 2 - 4
print(perimeter_trees)

# Print grid to visually see
for row in tree_grid:
    print(row)

inside_visible_trees = 0
for row_idx in range(1, row_stop_idx):
    for col_idx in range(1, col_stop_idx):
        tree_ht = tree_grid[row_idx][col_idx]

        trees_shorter = []
        for row_chng,col_chng in adj_tree_idxs:
            neighbor_tree_ht = tree_grid[row_idx + row_chng][col_idx + col_chng]

            trees_shorter.append(tree_ht >= neighbor_tree_ht)

        all_trees_shorter = all(trees_shorter)
        if all_trees_shorter:
            inside_visible_trees += 1
            print(f'Visible tree at [{row_idx}][{col_idx}]')


total_visible_trees = perimeter_trees + inside_visible_trees
print(f'Total visible trees in grid: {total_visible_trees}')

