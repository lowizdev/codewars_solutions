def up_array(arr):
    if(not valid_input_check(arr)):
        return None
    return recursive_add_one(arr, len(arr) - 1) #[int(x) for x in (str(int(''.join(map(str, arr))) + 1))]

def recursive_add_one(arr, index):
    
    if(index < 0):
        arr.insert(0,1)
        return arr
    arr[index] += 1
    if(arr[index] > 9):
        arr[index] = 0
        return recursive_add_one(arr, index - 1)
    return arr

def valid_input_check(arr):
    if(len(arr) == 0):
        return False
    for i in arr:
        if i < 0 or i > 9:
            return False
    return True