def same_structure_as(original,other): #SHOULD BE REFACTORED TO MAKE IT LESS CUMBERSOME

    if (is_arr(original) and is_arr(other) and len(original) != len(other)) or ((is_arr(original) or is_arr(other)) and (type(original) != type(other))): # (type(original) != type(other)) or
        return False
     
    for i, structure in enumerate(original):
        if i < len(other) and type(structure) in [int, str] and type(other[i]) in [int, str]: # doesnt differentiate scalar types
            continue
        elif type(structure) == type(other[i]) and is_arr(structure) and is_arr(other[i]) and len(structure) == len(other[i]):
            if(same_structure_as(structure, other[i])):
                continue
        return False
    return True

def is_arr(structure):
    return hasattr(structure, "__len__")