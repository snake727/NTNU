def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isPrimeReversed(n):
    reversed_n = 0
    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10

    if reversed_n <= 1:
        return False
    for i in range(2, reversed_n):
        if reversed_n % i == 0:
            return False
    return True
    
count = 0
primeholder = 1

while count < 20:
    if (isPrime(primeholder) == True) and (isPrimeReversed(primeholder) == True):
        print (f"{primeholder} is a prime both normally and reversed!")
        count += 1
    primeholder += 1

