def is_armstrong_number(number):
    y = len(str(number))
    arr = [int(digit) for digit in str(number)]
    total = 0 
    for i in range(0, y):
        total += arr[i]**y
    if total == number:
        return True   
    return False
