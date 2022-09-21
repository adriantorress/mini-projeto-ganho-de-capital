from Fila import *
from Deque import *

operacao = None
fila = FilaArray()
saldo = 0
lucro = 0
while operacao != 'fim':
    transacao = input("Digite 'compra' ou 'venda', qntd de ações, valor das ações OU FIM para finalizar as transações: ").split()
    if transacao[0].lower() != 'fim':
        operacao = transacao[0].lower(); acao = int(transacao[1]); valor = float(transacao[2])
    else: break

    if operacao == 'compra':
        for i in range(acao):
            fila.enqueue(valor)
            saldo -= valor

    elif operacao == 'venda':        
        for i in range(acao):
            lucro += valor - fila.dequeue()
            saldo += valor
    
    else:
        print("Operação inválida! Válidas: 'compra', 'venda' ou 'fim'.")

    print(fila)
    print("Saldo atual: R$ ", saldo)
    print("Lucro da venda da ação anterior: R$ ", lucro)