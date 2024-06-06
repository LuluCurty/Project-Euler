def is_multiple_of(number1, number2):
    sum = 0
    for x in range(2, 1000, 1):
        if not x % number1 or not x % number2:
            sum = x + sum
    return sum
print(f"the sum of the multiple of 3 and 5 1000 times is: {is_multiple_of(3, 5)}.")

# lesser
sumf = 0 
for x in range(1000):
    if not x % 3 or not x % 5:
            sumf = x + sumf
print(sumf)

# even lesser 

test = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
print(sum(test))
