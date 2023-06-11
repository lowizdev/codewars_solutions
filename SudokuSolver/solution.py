def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    
    constraints = [ row[:] for row in puzzle ]
    
    #validate_square(puzzle, 0, 4)
    
    #print(get_previous_index_avoiding_constraints(constraints, 2, 2))
    (row, column) = get_next_index_avoiding_constraints(constraints, 0, 0)
    #print(row, column)
    
    while(row < 9 and column < 9):
        #while():
        row, column = backtrack(puzzle, constraints, row, column, 1)
        print(row, column)
        row, column = get_next_index_avoiding_constraints(constraints, row, column + 1)
    
    '''for i, row in enumerate(puzzle):
        for j, line_item in enumerate(row):
            pass'''
            
    
    return puzzle

def backtrack(puzzle, constraints, row, column, assigned_value):
    
    puzzle[row][column] = assigned_value # should check if zero then assign 1?
    
    valid_row = validate_row(puzzle, row)
    valid_column = validate_column(puzzle, column)
    valid_square = validate_square(puzzle, row, column)
    
    if valid_row and valid_column and valid_square and assigned_value <= 9 and assigned_value > 0:
        print('RET', row, column)
        return (row, column)
    
    if assigned_value < 9: # exhausting options for that case
        return backtrack(puzzle, constraints, row, column, puzzle[row][column] + 1)
    
    #
    
    puzzle[row][column] = 0 # cleanup
    
    previous_index = get_previous_index_avoiding_constraints(constraints, row, column - 1)
    print('PREV:', previous_index)
    
    return backtrack(puzzle, constraints, previous_index[0], previous_index[1], puzzle[previous_index[0]][previous_index[1]] + 1)
    
    #print('TTT', previous_index[0], previous_index[1])
    '''if column == 0: #and row
        return backtrack(puzzle, constraints, row - 1, column, puzzle[row][column] + 1)
    return backtrack(puzzle, constraints, row, column - 1, puzzle[row][column] + 1)'''
    
    
def validate_row(puzzle, row):
    validated = set()
    for i in puzzle[row]:
        if i == 0:
            continue
        if i in validated:
            return False
        validated.add(i)
    return True

def validate_column(puzzle, column):
    validated = set()
    
    current_column = [row[column] for row in puzzle]
    
    #print(current_column)
    
    for i in current_column:
        if i == 0:
            continue
        if i in validated:
            return False
        validated.add(i)
    return True

def validate_square(puzzle, row, column):
    row_limits = get_box_limits(row)
    column_limits = get_box_limits(column)
    
    current_square = []
    for i in range(*row_limits):
        for j in range(*column_limits):
            current_square.append(puzzle[i][j])
    
    #print(current_square)
    
    validated = set()
    
    for i in current_square:
        if i == 0:
            continue
        if i in validated:
            return False
        validated.add(i)
    return True
    

def get_box_limits(index):
    if index < 3:
        return (0, 3)
    elif index < 6:
        return (3, 6)
    return (6, 9)

def get_next_index_avoiding_constraints(constraints, row, column):

    while(row < 9):
        while(column < 9):
            if constraints[row][column] == 0:
                return (row, column)
            column += 1
        column = 0
        row += 1
    return(9,0)
        
def get_previous_index_avoiding_constraints(constraints, row, column):

    while(row >= 0):
        while(column >= 0):
            if constraints[row][column] == 0:
                return (row, column)
            column -= 1
        column = 8
        row -= 1
            
    