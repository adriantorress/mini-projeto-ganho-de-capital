from Fila import *
from Deque import *

operacao = None
fila = FilaArray()
saldo = 0
while operacao != 'fim':
    transacao = input("Digite 'compra' ou 'venda', qntd de ações, valor das ações OU FIM para finalizar as transações: ").split()
    if transacao[0].lower() != 'fim':
        operacao = transacao[0].lower(); acao = int(transacao[1]); valor = float(transacao[2])
    operacao = transacao[0].lower()

    if operacao.lower() == 'compra':
        for i in range(acao):
            fila.enqueue(valor)
            saldo -= valor
    else:
        for i in range(acao):
            saldo += valor - fila.dequeue()

    print(fila)
    print(saldo)