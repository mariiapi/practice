def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def divided_by_5(n):
    if n%5 == 0:
        return "Is divided by 5"
    return "Is not divided by 5"

def is_prime(n):
    # Check if the number is less than 2 (not prime)
    if n <= 1:
        return False
    # Check if the number is 2 or 3 (prime numbers)
    if n <= 3:
        return True
    # Eliminate even numbers and numbers divisible by 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for other divisors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

