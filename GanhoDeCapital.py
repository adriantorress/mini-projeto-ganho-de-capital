from Fila import *
from Deque import *

def desfaz_operacao(fila):
    estado_anterior = deque.delete_last()
    if estado_anterior[0] == fila:
        estado_anterior[0] = deque.delete_last()
        fila = FilaArray(dados=estado_anterior[0])
        deque.add_last(estado_anterior)
    else:
        fila = FilaArray(dados=estado_anterior[0])
    return fila

def add_deque(fila, saldo, lucro):
    estado = [fila, saldo, lucro]
    if deque.size() <= 10:
        deque.add_last(estado)
    else:
        deque.delete_first()
        deque.add_last(estado)

operacao = None
fila = FilaArray()
saldo = 0
deque = DequeArray()

while operacao != 'fim':
    transacao = input(
        "Digite 'compra' ou 'venda', qntd de ações, valor das ações. 'FIM' ou '<' para finalizar as transações: ").split()
    if transacao[0].lower() != 'fim' and transacao[0].lower() != '<':
        operacao = transacao[0].lower()
        acao = int(transacao[1])
        valor = float(transacao[2])
        lucro = 0

        if operacao == 'compra':
            for i in range(acao):
                fila.enqueue(valor)
                saldo -= valor
            add_deque(fila.fila_to_list(), saldo, lucro)

        elif operacao == 'venda' and acao <= fila.size():
            for i in range(acao):
                lucro += valor - fila.dequeue()
                saldo += valor
            add_deque(fila.fila_to_list(), saldo, lucro)
        
        elif acao > fila.size():
            print(f"\nErro! você não possui ações suficientes para fazer esta operação!")
            print(f"Disponível: {fila.size()}")
        else:
            print("Operação inválida! Válidas: 'compra', 'venda', 'fim' ou '<'(desfazer operação anterior).")

    elif transacao[0] == '<':
        fila = desfaz_operacao(fila.fila_to_list())        
    else:
        break

    
    print()
    print(fila)
    print("Saldo atual: R$ ", saldo)
    print("Lucro da venda da ação anterior: R$ ", lucro)
    print()
    print(deque)
    print('---------------------------------------------------------------------------------------------------------------------------------')
