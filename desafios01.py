# COMENTARIO DE 1 LINHA
"""
comentario
de
varias
linhas

"""
print('====== DESAFIO05 ======')
num = int(input('Digite um número para ver seu sucessor e antecessor!: '))
su = num + 1
an = num - 1
print('O sucessor desse número é {}, e o antecessor é {}.'.format(su, an))

print('====== DESAFIO06 ======')
numero = int(input('Digite um número para ver seu dobro, triplo e sua raiz quadrada: '))
db = numero * 2
tp = numero * 3
rq = numero**(1/2)
print('O dobro desse número é {}, o tripo é {}, e a raiz quadrada é {}.'.format(db, tp, rq))

print('====== DESAFIO07 ======')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunta nota: '))
media = (nota1 + nota2)/2
print('Sua media entre essas duas notas é {}.'.format(media))


print('====== DESAFIO08 ======')
metros = float(input('Digite um numero em metros para ver quanto o mesmo vale em centímetros e milímetros: '))
cm = metros*100
mm = cm*10
print('Esse número vale {}cm e {}mm.'.format(cm, mm))


print('====== DESAFIO09 ======')
nb = float(input('Digite um número para ver sua respectiva tabuada: '))
n1 = nb * 1
n2 = nb * 2
n3 = nb * 3
n4 = nb * 4
n5 = nb * 5
n6 = nb * 6
n7 = nb * 7
n8 = nb * 8
n9 = nb * 9
n10 = nb * 10
print('1|  {}'.format(n1))
print('2|  {}'.format(n2))
print('3|  {}'.format(n3))
print('4|  {}'.format(n4))
print('5|  {}'.format(n5))
print('6|  {}'.format(n6))
print('7|  {}'.format(n7))
print('8|  {}'.format(n8))
print('9|  {}'.format(n9))
print('10| {}'.format(n10))


print('====== DESAFIO010 ======')
reais = float(input('Digite quantos reais você tem para ver quantos dolares você pode comprar: '))
dollares = reais/3.27
print('Você pode comprar U${:.2f} em dolar.'.format(dollares))


print('====== DESAFIO011 ======')
l = float(input('Digite o comprimento em metros da parede: '))
h = float(input('Digite a altura em metros da parede: '))
area = l*h
qt = area/2
print('A área da sua parede é de {}m², sendo que você precisará de {}L de tinta para pinta-la por completo.'.format (area, qt))


print('====== DESAFIO012 ======')
preçoProduto = float(input('Digite o preço do produto: '))
dx = (preçoProduto*5)/100
print('O preço desse produto com um desconto de 5% é R${:.2f}'.format(dx))


