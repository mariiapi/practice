def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def divided_by_5(n):
    if n%5 == 0:
        return "Is divided by 5"
    return "Is not divided by 5"