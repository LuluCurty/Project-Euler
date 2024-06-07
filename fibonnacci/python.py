def fibonacci():
    num1, num2, temp, fib_array = 0, 1, 0, [0]
    while (num2 < 4000000):
        if not num2 % 2:
            fib_array.append(num2)
        num1, num2 = num2, num1 + num2
    return sum(fib_array)
print(f"{fibonacci()}")











num1, num2, temp, fib_array = 0, 1, 0, [0]
while (num2 < 4000000):
    if not num2 % 2:
        fib_array.append(num2)
    num1, num2 = num2, num1 + num2
print(f"The sum of the fib function is {sum(fib_array)}")