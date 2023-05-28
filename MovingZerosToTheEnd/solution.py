def move_zeros(lst):
    counter = 0
    zero_counter = 0
    while counter < len(lst):
        if lst[counter] == 0:
            zero_counter += 1
        counter+=1
    return ([i for i in lst if i != 0]) + ([0] * zero_counter) 