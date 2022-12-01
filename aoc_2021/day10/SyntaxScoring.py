'''
Determine which chunks of syntax
are corrupt or incomplete.

Austin Equitz
austin.equitz@gmail.com
'''

# Check for balanced parentheses
def checkSyntax(syntax: str) -> tuple:
    open_brackets = ['(', '{', '[', '<']
    closing_brackets = [')', '}', ']', '>']

    bad_br = ""
    incomplete = ""

    while syntax:
        close_idxs = [idx for idx,chr in enumerate(syntax) if chr in closing_brackets]
        
        if close_idxs:

            open_br = open_brackets[closing_brackets.index(syntax[close_idxs[0]])]
            close_br = syntax[close_idxs[0]]

            if syntax[close_idxs[0] - 1] == open_br:
                syntax = syntax.replace(open_br + close_br, "")

            else:
                bad_br = close_br
                break
        
        else:
            incomplete = syntax
            break
    
    if bad_br == ')':
        points = 3
    elif bad_br == ']':
        points = 57
    elif bad_br == '}':
        points = 1197
    elif bad_br == '>':
        points = 25137
    else:
        points = 0

    return bad_br, incomplete, points

def completeSyntax(syntax: str) -> tuple:
    open_brackets = ['(', '{', '[', '<']
    closing_brackets = [')', '}', ']', '>']

    points = 0
    missing_brackets = ""

    for char in syntax[::-1]:
        close_br = closing_brackets[open_brackets.index(char)]
        missing_brackets += close_br

        if close_br == ')':
            point = 1
        elif close_br == ']':
            point = 2
        elif close_br == '}':
            point = 3
        elif close_br == '>':
            point = 4
        else:
            point = 0
        
        points = points * 5 + point

    return points, missing_brackets



if __name__ == '__main__':
    with open('InputSyntax.txt', 'r') as fin: syntax_in = [x for x in fin.read().split()]

    # Part 1: Determine score of corrupted lines and get list of incomplete lines
    total_points = 0
    incomplete_lines = []

    
    for line in syntax_in:
        bad_br,incomplete,points = checkSyntax(line)

        if incomplete: incomplete_lines.append(incomplete)

        total_points += points

    print(incomplete_lines)
    print(total_points)

    # Part 2: Find missing brackets for all incomplete lines and report middle score
    incomplete_points = []
    all_missing_brackets = []

    for line in incomplete_lines:
        points,missing_brackets = completeSyntax (line)

        incomplete_points.append(points)
        all_missing_brackets.append(missing_brackets)

    incomplete_points.sort()
    all_missing_brackets.sort()

    print(incomplete_points[int(len(incomplete_points)/2)])
    print(all_missing_brackets)