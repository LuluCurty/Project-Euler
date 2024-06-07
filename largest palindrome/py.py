def largest_palindrome():
    number, p, lp = 0, 0, 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            number = x * y  
            if(str(number) == str(number)[::-1]):
                p = number
                if(p > lp): lp = p
    return lp
    
largest_palindrome()
