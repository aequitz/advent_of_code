'''
Day 8: Treetop Tree House

Austin Equitz
austin.equitz@gmail.com
'''
import math
import numpy as np

with open('tree_grid.txt', 'r') as fin: tree_input = fin.read().splitlines()

tree_grid = np.array([[int(char) for char in line] for line in tree_input])

# Get stop indexes so outer border of trees is ignored
num_rows = len(tree_grid)
num_cols = len(tree_grid[0])
row_stop_idx = num_rows - 1
col_stop_idx = num_rows - 1

# Calculate perimeter trees
perimeter_trees = num_rows * 2 + num_cols * 2 - 4

# Initialize loop variables
inside_visible_trees = 0
scenic_scores = []

# Iterate through all inner trees (not including perimeter)
for row_idx in range(1, row_stop_idx):
    for col_idx in range(1, col_stop_idx):
        current_tree = tree_grid[row_idx, col_idx]

        # Create lists of each tree line direction
        north_trees = np.flip(tree_grid[0:row_idx, col_idx])
        east_trees = tree_grid[row_idx, col_idx + 1:]
        south_trees = tree_grid[row_idx + 1:, col_idx]
        west_trees = np.flip(tree_grid[row_idx, 0:col_idx])

        visible_tree_lines = []
        viewing_distances = []
        for tree_dirs in [north_trees, east_trees, south_trees, west_trees]:

            # Determine if each line to the edge of the trees makes
            # the current tree visible
            visible_line = all(tree < current_tree for tree in tree_dirs)
            visible_tree_lines.append(visible_line)

            # Find index of tree that blocks from the edges
            blocking_tree_idx =  next((i for i,v in enumerate(tree_dirs) if v >= current_tree), None)

            # Add the number of trees visible in the current tree line
            if blocking_tree_idx != None:
                viewing_dist = blocking_tree_idx + 1
            else:
                viewing_dist = len(tree_dirs)

            viewing_distances.append(viewing_dist)

        # Add tree to visible trees if any tree line causes it to be visible from the edge
        if any(visible_tree_lines): inside_visible_trees += 1

        # Append the scenic score
        scenic_score = math.prod(viewing_distances)
        scenic_scores.append(scenic_score)

total_visible_trees = perimeter_trees + inside_visible_trees
print(f'Total visible trees in grid: {total_visible_trees}')

max_scenic_score = max(scenic_scores)
print(f'The highest scenic score: {max_scenic_score}')

