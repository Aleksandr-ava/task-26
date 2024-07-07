def is_prime(func):
    def wrapper(a, b, c):
        if func(a, b, c) % func(a, b, c) == 0 and func(a, b, c) != 0:
            return print('Простое\n', func(a, b, c))
        else:
            return print('Составное\n', func(a, b, c))
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
