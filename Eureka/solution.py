def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    result = []
    for i in range(a, b + 1):
        digits = [int(j) for j in str(i)]
        digit_sum = 0
        for index, digit in enumerate(digits, start=1):
            digit_sum += (digit ** index)
        if(digit_sum == i):
            result.append(i)
    return result