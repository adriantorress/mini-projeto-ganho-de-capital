from Fila import *
from Deque import *


def desfaz_operacao(fila, deque, desfazer):
    removido = deque.delete_last()
    try:
        desfazer += 1
        estado_atual = deque.delete_last()
        saldo = estado_atual[1]
        lucro = estado_atual[2]
        acao_comprada_qntd = estado_atual[3]
        fila = FilaArray(dados=estado_atual[0])
        deque.add_last(estado_atual)
        return fila, deque, saldo, lucro, acao_comprada_qntd, desfazer
    except(DequeVazio):
        if desfazer > 10:
            print("\nOperação não permitida.\n")
            fila = FilaArray(dados=removido[0])
            saldo = removido[1]
            lucro = removido[2]
            acao_comprada_qntd = removido[3]
            if len(deque) == 0:
                deque.add_last(removido)
            return fila, deque, saldo, lucro, acao_comprada_qntd, desfazer
        else:
            fila = FilaArray()
            saldo = 0
            lucro = 0
            acao_comprada_qntd = 0
            return fila, deque, saldo, lucro, acao_comprada_qntd, desfazer


def add_deque(fila, saldo, lucro, acao_comprada_qntd):
    estado = [fila, saldo, lucro, acao_comprada_qntd]
    deque.add_last(estado)


operacao = None
fila = FilaArray()
saldo = 0
deque = DequeArray()
desfazer = 0
acao_comprada_qntd = 0

while operacao != 'fim':
    transacao = input(
        "\n---------------------------------------------------------------------------------------------------------------------------------\nDigite 'compra' ou 'venda', qntd de ações, valor das ações; '<' para cancelar a transação anterior ou 'FIM' para finalizar as transações: ").split()
    try:
        if transacao[0].lower() != 'fim' and transacao[0].lower() != '<':
            try:
                operacao = transacao[0].lower()
                acao = int(transacao[1])
                valor = float(transacao[2])
                lucro = 0

                if operacao != 'compra' and operacao != 'venda':
                    print(
                        "\nOperação inválida! Válidas: 'compra' ou 'venda'.  '<' para desfazer a transação anterior ou 'fim' para finalizar as transações.\n")
                    continue

                if acao <= 0 or valor <= 0:
                    print(
                        "\nOs valores inseridos para quantidade de ações e/ou preço devem ser maiores que zero.\n")
                    continue

                elif operacao == 'compra':
                    if desfazer > 0:
                        desfazer -= 1
                    compra = [acao, valor]
                    saldo -= acao*valor
                    fila.enqueue(compra)
                    acao_comprada_qntd += acao
                    add_deque(fila.fila_to_list(), saldo,
                              lucro, acao_comprada_qntd)

                elif operacao == 'venda' and acao <= acao_comprada_qntd:
                    if desfazer > 0:
                        desfazer -= 1

                    while acao != 0:
                        venda = fila.dequeue()
                        acao_vendida_qntd = venda[0]
                        acao_vendida_valor = venda[1]

                        if acao_vendida_qntd <= acao:
                            lucro += (acao_vendida_qntd*valor) - \
                                (acao_vendida_qntd*acao_vendida_valor)
                            acao -= acao_vendida_qntd
                            saldo += (acao_vendida_qntd*valor)
                            acao_comprada_qntd -= acao_vendida_qntd
                        else:
                            acao_vendida_qntd -= acao
                            lucro += (acao*valor)-(acao*acao_vendida_valor)
                            saldo += (acao*valor)
                            acao_comprada_qntd -= acao
                            acao = 0
                            restante = [
                                [acao_vendida_qntd, acao_vendida_valor]]

                            restante.extend(fila.fila_to_list())
                            fila = FilaArray(dados=restante)

                    add_deque(fila.fila_to_list(), saldo,
                              lucro, acao_comprada_qntd)

                elif operacao == 'venda' and acao > acao_comprada_qntd:
                    print(
                        f"\nVocê não possui ações suficientes para fazer esta transação.")
                    print(f"Ações disponíveis: {acao_comprada_qntd} ações.")
                    print('Tente novamente.\n')
                    continue

            except:
                print("\nOperação inválida! Válidas: 'compra' ou 'venda'.  ' < ' para desfazer a transação anterior ou 'fim' para finalizar as transações.\n")
                continue

        elif transacao[0] == '<':
            try:
                fila, deque, saldo, lucro, acao_comprada_qntd, desfazer = desfaz_operacao(
                    fila.fila_to_list(), deque, desfazer)
            except(DequeVazio):
                print("\nOperação não permitida.\n")
                valor_acoes = 0
                for acao in acoes:
                    valor_acoes += acao[0]*acao[1]
                print(f'\nSaldo das transações: R${saldo}')
                print("Quantidade de ações: ", acao_comprada_qntd)
                print(f'Saldo em ações: R${valor_acoes}\n')
                continue

        acoes = fila.fila_to_list()
        valor_acoes = 0
        for acao in acoes:
            valor_acoes += acao[0]*acao[1]
        if lucro > 0:
            print(f"\nLucro da última transação: R${lucro}")
        elif lucro < 0:
            print(f"\nPrejuízo da última transação: R${-lucro}")

        if saldo >= 0:
            print(f'\nSaldo das transações: R${saldo}')
        elif saldo < 0:
            print(f'\nSaldo das transações: -R${-saldo}')
        print("Quantidade de ações: ", acao_comprada_qntd)
        print(f'Saldo em ações: R${valor_acoes}\n')

    except(IndexError):
        print("\nDigite uma transação válida.")
