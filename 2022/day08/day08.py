def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def get_rows_and_columns(text):

    rows = text.split('\n')
    length = len(rows[0])
    
    cols = []
    index = 0
    for column in range(1, length):
        tmp = ""
        for row in rows:
            # get the index number and add it to the cols
            tmp += row[index] # This adds the <index>th number to the <column> in cols
        index += 1
        cols.append(tmp)

    
    
    return (rows, cols)


# All the edges are visisble

# Start from the edges and move inwards

# Starting from the top:
    # call check view:
        # Check view will scan each direction to see if there are any values that are greater than the current tree

def check_tree_view(r, c):
    print(f"Looking at tree {r[c]}")

    return False

def main(trees):

    trees_visible = 0
    # Top row is in view
    trees_visible += len(trees[0][0])
    # Now iterate though the next row
    row = 0
    for row in trees[0][1:]:
        x_position = 0
        for tree in row:       
            
            # Check if tree is on a side
            if (row == 0) or (row == 99) or (x_position == 0) or (x_position == 99):
                tress_visible += 1
                continue
            # Check if there is a taller tree on right and left of current tree
            distance = 1
            for position in row:
                if (tree > row[x_position + 1])


            check_tree_view(row, trees[1][x_position])
        row += 1
    
    
    return trees_visible








if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()

    trees = get_rows_and_columns(f)

    print(main(trees))