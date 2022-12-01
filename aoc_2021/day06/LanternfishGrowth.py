'''
Determine the number of lanternfish that
grow over a given number of days

Austin Equitz
austin.equitz@gmail.com
'''

with open('FishInput.txt', 'r') as fin: fish_in = [int(n) for n in fin.read().split(',')]

'''
# Lessons Learned: This section of code results in memory overflow
# due to an exponentially increasing list. Since the objective is
# to keep track of the number of fish and not necessarily each fish's
# number, it is best to create a count for each number type.

for days in range(256):
    new_fish = 0

    for idx in range(len(fish_in)):
        new_fish = ((new_fish + 1) if fish_in[idx] == 0 else new_fish)
        fish_in[idx] = (6 if fish_in[idx] == 0 else (fish_in[idx] - 1))

    fish_in = (fish_in + [8] * new_fish)

print(len(fish_in))
'''

counts = [0] * 9

for fish in fish_in:
    counts[fish] += 1

for days in range(256):
    new_fish = counts[0]

    for c in range(1, 7):
        counts[c - 1] = counts[c]
    
    counts[6] = counts[7] + new_fish
    counts[7] = counts[8]
    counts[8] = new_fish

print(sum(counts))