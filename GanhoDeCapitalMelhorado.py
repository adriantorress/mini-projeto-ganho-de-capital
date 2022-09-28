from Fila import *
from Deque import *


# Adiciona os dados no deque
def add_ctrl_z(estado, saldo, lucro, acao_comprada_qntd):
    estado = [estado, saldo, lucro, acao_comprada_qntd]
    deque.add_last(estado)


def desfaz_operacao(fila, deque):
    removido = deque.delete_last()
    try:
        global desfazer
        desfazer += 1
        estado_atual = deque.delete_last()
        saldo = estado_atual[1]
        lucro = estado_atual[2]
        acao_comprada_qntd = estado_atual[3]
        fila = FilaArray(dados=estado_atual[0])
        deque.add_last(estado_atual)
        return fila, deque, saldo, lucro, acao_comprada_qntd
    except(DequeVazio):
        if len(deque) <= 1 and len(fila) > 1 and desfazer > 9:
            print("\nOperação não permitida.\n")
            fila = FilaArray(dados=removido[0])
            saldo = removido[1]
            lucro = removido[2]
            acao_comprada_qntd = removido[3]
            if len(deque) == 0:
                deque.add_last(removido)
            return fila, deque, saldo, lucro, acao_comprada_qntd
        else:
            fila = FilaArray()
            saldo = 0
            lucro = 0
            acao_comprada_qntd = 0
            return fila, deque, saldo, lucro, acao_comprada_qntd


# Inicio:
operacao = None
fila = FilaArray()
saldo = 0
deque = DequeArray()
global desfazer
desfazer = 0
acao_comprada_qntd = 0

while operacao != 'fim':
    # Input:
    transacao = input("'compra' ou 'venda' qntd de ações valor das ações; '<' para cancelar a transação anterior; 'FIM' para finalizar as transações: ").split()

    if transacao[0].lower() != 'fim' and transacao[0].lower() != '<':
        try:
            # Separação dos valores em variaveis
            operacao = transacao[0].lower()
            acao = int(transacao[1])
            valor = float(transacao[2])
            lucro = 0

            if acao <= 0 or valor <= 0:
                print("Os valores inseridos para quantidade de ações e/ou preço devem ser maiores que zero. Insira dados corretos.")
                continue
            # Compra
            elif operacao == 'compra':
                if desfazer > 0:
                    desfazer -= 1

                compra = [acao, valor]
                saldo -= acao*valor
                fila.enqueue(compra)
                acao_comprada_qntd += acao
                add_ctrl_z(fila.fila_to_list(), saldo, lucro, acao_comprada_qntd)

            # Venda
            elif operacao == 'venda' and acao <= acao_comprada_qntd:                
                if desfazer > 0:
                    desfazer -= 1
                # Redução das vendas das ações até que se venda a quantidade de ações informada.
                while acao != 0:
                    # IMPORTANTE! a variavel venda está armazenada em um espaço de memoria de um objeto.
                    # manipular as posições dela (venda[0] e venda[1]) no restante do código afetará os estados anteriores do deque.
                    venda = fila.dequeue()
                    acao_vendida_qntd = venda[0]
                    acao_vendida_valor = venda[1]

                    # Caso a quantidade de ações removidas da fila seja menor ou igual a quantidade de ações que pretende-se vender.
                    if acao_vendida_qntd <= acao:
                        lucro += (acao_vendida_qntd*valor)-(acao_vendida_qntd*acao_vendida_valor)
                        acao -= acao_vendida_qntd
                        saldo += (acao_vendida_qntd*valor)
                        acao_comprada_qntd -= acao_vendida_qntd

                    # Caso a quantidade de ações removidas da fila seja maior que a quantidade que pretende-se vender.
                    # Faz-se necessario "atualizar" a primeira posição da fila para ser a quantidade restante das ações.
                    # "atualizar" entre aspas pois aqui a fila está sendo refeita.
                    else:
                        acao_vendida_qntd -= acao
                        lucro += (acao*valor)-(acao*acao_vendida_valor)
                        saldo += (acao*valor)
                        acao_comprada_qntd -= acao 
                        acao = 0
                        # Salva oq sobrou das ações numa nova lista, ou seja posição 0                                     
                        restante = [[acao_vendida_qntd, acao_vendida_valor]]
                        # Junta todo o resto da fila na lista acima.
                        restante.extend(fila.fila_to_list())
                        fila = FilaArray(dados=restante)

                add_ctrl_z(fila.fila_to_list(), saldo, lucro, acao_comprada_qntd)
            
            elif operacao == 'venda' and acao > acao_comprada_qntd:
                print("\nVocê não possui ações suficientes para realizar está operação! Tente novamente.")
                print(f"Quantidade de ações disponiveis: {acao_comprada_qntd}")

            else:
                print("Operação inválida! Válidas: 'compra' ou 'venda'. '<' para desfazer a transação anterior ou 'fim' para finalizar as transações.")
                continue
                        
        except:
            print('Alguma ação inválida, tente novamente\n')
            continue

    elif transacao[0] == '<':
        try:
            fila, deque, saldo, lucro, acao_comprada_qntd = desfaz_operacao(fila.fila_to_list(), deque)
        except(DequeVazio):
            print("\nOperação não permitida.\n")
            print(fila)
            print("Saldo atual: R$ ", saldo)
            print()
            print('---------------------------------------------------------------------------------------------------------------------------------')
            continue
    
    elif transacao[0].lower() == 'fim':
        break

    print()
    print(fila)
    print("Saldo atual: R$ ", saldo)
    print("Lucro da transação anterior: R$ ", lucro)
    print()
    # print(deque)
    print('---------------------------------------------------------------------------------------------------------------------------------')