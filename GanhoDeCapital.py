from Fila import *
from Deque import *


def desfaz_operacao(fila, deque):
    removido = deque.delete_last()
    try:
        estado_atual = deque.delete_last()
        saldo = estado_atual[1]
        lucro = estado_atual[2]
        fila = FilaArray(dados=estado_atual[0])
        deque.add_last(estado_atual)
        return fila, deque, saldo, lucro
    except(DequeVazio):
        fila = FilaArray(dados=removido[0])
        saldo = removido[1]
        lucro = removido[2]
        return fila, deque, saldo, lucro


def add_deque(fila, saldo, lucro):
    estado = [fila, saldo, lucro]
    deque.add_last(estado)

operacao = None
fila = FilaArray()
saldo = 0
deque = DequeArray()

while operacao != 'fim':
    transacao = input(
        "Digite 'compra' ou 'venda', qntd de ações, valor das ações; '<' para cancelar a transação anterior ou 'FIM' para finalizar as transações: ").split()
    if transacao[0].lower() != 'fim' and transacao[0].lower() != '<':
        try:
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
                saldo_anterior = saldo
                for i in range(acao):
                    lucro +=valor - fila.dequeue()
                    saldo += valor
                add_deque(fila.fila_to_list(), saldo, lucro)

            elif operacao == 'venda' and acao > fila.size():
                print(
                    f"\nVocê não possui ações suficientes para fazer esta transação.")
                print(f"Ações disponíveis: {fila.size()} ações.")
                print('Tente novamente.\n')
                continue
            else:
                print(
                    "Operação inválida! Válidas: 'compra' ou 'venda'.  '<' para desfazer a transação anterior ou 'fim' para finalizar as transações.")
                continue
        except:
            print('Alguma ação inválida, tente novamente\n')
            continue

    elif transacao[0] == '<':
        try:
            fila, deque, saldo, lucro = desfaz_operacao(
                fila.fila_to_list(), deque)
        except(DequeVazio):
            print("\nVocê não tem nenhuma transação.\n")
            print(fila)
            print("Saldo atual: R$ ", saldo)
            print()
            continue

    elif transacao[0] == '<':
        fila = desfaz_operacao(fila.fila_to_list())        
    else:
        break

    print()
    print(fila)
    print("Saldo atual: R$ ", saldo)
    print("Lucro da transação anterior: R$ ", lucro)
    print()
    print(deque)
    print('---------------------------------------------------------------------------------------------------------------------------------')
