def prime_factor(number: int):
    count, primes = 2, []
    while(count <= number):
        if not number % count:
            primes.append(count)
            number = number / count
        else:
            count = count + 1
    return primes   