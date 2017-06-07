'''
---------- PROGRAMAÇÃO DINAMICA --------

Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34...

Definição: F(n) = F(n-1) + F(n-2)
'''


def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_rapido(n):
    if n ==1 or n ==2:
        return 1
    f1 = 1
    f2 = 1
    for i in range(3, n+1):
        f = f1 + f2
        f2 = f1
        f1 = f
    return f1

print('Calculando o fib de forma lenta...')
print(fib(40))
print('Calculando o fib de forma rapida...')
print(fib_rapido(40))
