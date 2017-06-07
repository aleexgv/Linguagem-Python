'''
Algoritmos gulosos
- Sempre escolhe a alternativa mais promissora naquele instante
- NUNCA reconsidera essa decisão
- Uma escolha que foi feita nunca é revista
- Não há backtracking
- A escolha é feita de acordo com um criterio guloso
- Nem sempre dão soluções ótimas

Problema do troco(troco mínimo)
Moedas = {100, 50, 25, 5, 1}
troco: 75
Quantidade mínima de moedas: 2(1 de 50 + 1 de 25)

'''

moedas = [100, 50, 25, 5, 1]
total = 0
troco_inicial = 75
troco = troco_inicial

for i in range(len(moedas)):
    num_moedas = troco // moedas[i]
    troco -= num_moedas * moedas[i]
    total += num_moedas

print('O total de moedas minimas para dar o troco de {} é de {} moedas.'.format(troco_inicial, total))


