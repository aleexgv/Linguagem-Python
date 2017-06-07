'''
---------- PROGRAMAÇÃO DINAMICA -> PARTE 2  --------

Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34...

Definição: F(n) = F(n-1) + F(n-2)
'''

MAX_N = 100

n = 100 # range do nosso vetor
valores = [0] * n
valores[0] = valores[1] = 1

# recursivo lento - complexidade exponencial - O(2^n)
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)



# iterativo - complexidade linear - O(n)
def fib_rapido(n):
    if n > 100:
        print("Valor maximo de n tem que ser 100!")
    else:
        if valores[n - 1] != 0:
            print('Fib de %d, valor já calculado...' % n)
            return valores[n-1]
        else:
            print('Calculando o fib de %d...' % n)
            for i in range(2, n):
                valores[i] = valores[i - 1] + valores[i - 2]
            return valores[n - 1]



#print('Calculando o fib de forma lenta...')
#print(fib(40))
print('Calculando o fib de forma rapida...')
print(fib_rapido(20))
print(fib_rapido(10))
print(fib_rapido(30))
print(fib_rapido(50))
