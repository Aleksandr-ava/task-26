from math import sqrt


def is_prime(func):
    def wrapper(a, b, c=func):
        prime = True
        n = a + b + c
        i = 2
        while i <= sqrt(n):
            if n % i == 0:
                prime = False
                break
            i += 1
        if prime:
            print('Простое число\n', n)
        else:
            print('Составное число\n', n)
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 2, 2)
