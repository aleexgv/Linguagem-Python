lista = [30, 40, 10, 35, 70, 45, 80, 100, 22]
tam_lista = len(lista)

#burble sort
for i in range(tam_lista):
    troca = False
    for j in range(1, tam_lista - i):
        if lista[j] < lista[j-1]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            troca = True
    if not troca:
        break

print(lista)
