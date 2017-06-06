print("Hello world!")

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
soma = a+b
print('A soma é = {}'.format(a+b))

print("-------TIPOS PRIMITIVOS------")
algo = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(algo))
print('So tem espaços?', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalnum())
print('Está em minúscula? ', algo.islower())
print('Está em maiúscula? ', algo.isupper())
print('Está capitalizada? ', algo.istitle())
