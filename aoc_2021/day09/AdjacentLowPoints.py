'''
Determine the numbers that are lower
than all other adjacent numbers.
Add 1 to each of the numbers and sum all numbers.

Austin Equitz
austin.equitz@gmail.com
'''

with open('HeightMap.txt', 'r') as fin: height_map = [list(map(int, n)) for n in fin.read().splitlines()]

low_points = []
for row_idx,row in enumerate(height_map):

    for col_idx,num in enumerate(row):
        # Create logic to determine the num location
        top = (row_idx == 0)
        bottom = (row_idx == len(height_map) - 1)
        left = (col_idx == 0)
        right = (col_idx == len(row) - 1)
        
        # Get adjacent nums based on index
        adj_nums = []
                
        if not top:
            top_num = height_map[row_idx - 1][col_idx]
            adj_nums.append(top_num)

        if not bottom:
            bottom_num = height_map[row_idx + 1][col_idx]
            adj_nums.append(bottom_num)

        if not left:
            left_num = row[col_idx - 1]
            adj_nums.append(left_num)
            
        if not right:
            right_num = row[col_idx + 1]
            adj_nums.append(right_num)
        
        if all(num < adj_num for adj_num in adj_nums):
            low_points.append(num)

# Add 1 to all low points and sum
print(sum(map(lambda x:x+1, low_points)))