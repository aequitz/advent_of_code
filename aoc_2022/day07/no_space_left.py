'''
Day 7: No Space Left On Device

Austin Equitz
austin.equitz@gmail.com
'''
import re

import treelib

CD_CMD_REGEX = r'\$ cd '
LS_CMD_REGEX = r'\$ ls'
DIR_CMD = 'dir '
FILE_REGEX = r'([0-9]+) (.+)'
PARENT_DIR = '..'
MAX_DIR_SIZE = 100000
TOTAL_SPACE_AVAIL = 70000000
SPACE_REQUIRED = 30000000

with open('terminal_output.txt', 'r') as fin: term_out = fin.read().splitlines()

tree = treelib.Tree()
tree_id = tree.identifier
parent_node = None

# Create the tree of files/directories
for node_id, line in enumerate(term_out):
    print(line)
    node_to_create = file_data = None
    node_id = str(node_id)

    # Update parent node on cd command
    if re.search(CD_CMD_REGEX, line):
        dir_name = re.sub(CD_CMD_REGEX, '', line)

        if dir_name == PARENT_DIR:
            parent_id = parent_node.predecessor(tree_id)
            parent_node = tree.get_node(parent_id)

        elif not parent_node:
            parent_node = tree.create_node(dir_name, node_id, parent=parent_node)
            print(f'Child node {dir_name} not found. Node created.')

        else:
            child_nodes = [tree.get_node(x) for x in parent_node.successors(tree_id)]
            parent_node = next(x for x in child_nodes if x.tag == dir_name)

    # Do nothing on ls command
    elif re.search(LS_CMD_REGEX, line): pass

    # Parse directory name and prep node to be created
    elif line.startswith(DIR_CMD):
        dir_name = line.replace(DIR_CMD, '')
        node_to_create = dir_name

    # Parse file size and name and prep node to be created
    elif re.search(FILE_REGEX, line):
        all_data = re.search(FILE_REGEX, line).groups()
        file_data, file_name = re.search(FILE_REGEX, line).groups()
        node_to_create = file_name

    # Create node
    if node_to_create:
        tree.create_node(node_to_create, node_id, data=file_data, parent=parent_node)

tree.show()

# Find nodes without data which are directory nodes
dir_nodes = [x for x in tree.all_nodes() if x.data == None]

# Get the total size of each directory by summing up file data
dir_sizes = []
for dir_node in dir_nodes:
    dir_id = dir_node.identifier
    dir_name = dir_node.tag
    dir_tree = tree.subtree(dir_id)

    dir_size = sum([int(x.data) for x in dir_tree.all_nodes() if x.data != None])
    dir_sizes.append(dir_size)

# Only add up directories less than the MAX_DIR_SIZE
summed_max_dirs = sum([x for x in dir_sizes if x <= MAX_DIR_SIZE])
print(f'The total of summed directories with an individual max size of {MAX_DIR_SIZE}: {summed_max_dirs}')

# Part Two
# Get total size of directories
root_dir_size = max(dir_sizes)

# Calculate the minimum directory size that must be deleted
curr_avail_space = TOTAL_SPACE_AVAIL - root_dir_size
dir_size_to_delete = root_dir_size + SPACE_REQUIRED - TOTAL_SPACE_AVAIL

# Find the smallest directory size that can be deleted
avail_dirs_to_delete = [x for x in dir_sizes if x >= dir_size_to_delete]
avail_dirs_to_delete.sort()
dir_to_delete = avail_dirs_to_delete[0]

print(f'The size of the directory to be deleted: {dir_to_delete}')