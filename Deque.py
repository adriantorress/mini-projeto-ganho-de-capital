class DequeVazio(Exception):
    pass


class DequeArray:
    def __init__(self, capacidade=10):
        self._dados = [None] * capacidade
        self._tamanho = 0
        self._inicio = 0

    def __len__(self):
        return self._tamanho

    def size(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0

    def first(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        return self._dados[self._inicio]

    def last(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        return self._dados[(self._tamanho-1)]

    def delete_first(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        if 0 < self._tamanho <= (len(self._dados) // 4):
            self._altera_tamanho(len(self._dados) // 2)
        result = self._dados[self._inicio]
        dados = self._dados[:]
        posicao = self._inicio
        for k in range(self._tamanho):
            self._dados[k] = dados[posicao+1]
            posicao = (1 + posicao) % len(dados)
        self._inicio = 0
        self._tamanho -= 1
        return result

    def delete_last(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        if 0 < self._tamanho <= (len(self._dados) // 4):
            self._altera_tamanho(len(self._dados) // 2)
        result = self._dados[(self._tamanho-1)]
        self._dados[(self._tamanho-1)] = None
        self._tamanho -= 1
        return result

    def add_first(self, e):
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))
        dados = self._dados[:]
        posicao = self._inicio
        for k in range(self._tamanho+1):
            if posicao == self._inicio:
                self._dados[k] = e
            else:
                self._dados[k] = dados[posicao-1]
            posicao = (1 + posicao) % len(dados)

        self._inicio = 0
        self._tamanho += 1

    def add_last(self, e):
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1

    def _altera_tamanho(self, novo_tamanho):
        dados_antigos = self._dados
        self._dados = [None] * novo_tamanho
        posicao = self._inicio
        for k in range(self._tamanho):
            self._dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0

    def show(self):
        print(self)

    def __str__(self):
        posicao = self._inicio
        result = "["
        for k in range(self._tamanho):
            if k == (self._tamanho-1):
                result += str(self._dados[posicao])
            else:
                result += str(self._dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self._dados)
        result += f'] tamanho: {len(self)}, capacidade: {len(self._dados)}\n'
        return result


if __name__ == "__main__":
    deque = DequeArray()

    if deque.is_empty() == True:
        print("O Deque está vazio")

    print()
    print()

    deque.add_first(5)
    deque.add_last(10)
    deque.add_first(15)
    deque.add_last(20)
    deque.add_first(25)

    print('Deque: ', deque)
    print('First: ', deque.first())
    print('Last: ', deque.last())
    print('Tamanho: ', len(deque))
    print('Size: ', deque.size())
    print()
    print()

    deque.add_last(30)
    deque.add_first(35)
    deque.add_last(40)
    deque.add_first(45)
    deque.add_last(50)
    deque.add_first(55)
    deque.add_last(60)

    print('Show: ', end=' ')
    deque.show()
    print('First: ', deque.first())
    print('Last: ', deque.last())
    print('Tamanho: ', len(deque))
    print('Size: ', deque.size())
    print()
    print()

    deque.delete_first()
    deque.delete_last()

    print('Show: ', end=' ')
    deque.show()
    print('First: ', deque.first())
    print('Last: ', deque.last())
    print('Tamanho: ', len(deque))
    print('Size: ', deque.size())
    print()
    print()

    deque.delete_first()
    deque.delete_last()

    print('Show: ', end=' ')
    deque.show()
    print('First: ', deque.first())
    print('Last: ', deque.last())
    print('Tamanho: ', len(deque))
    print('Size: ', deque.size())
    try:
        deque.is_empty()
        print("Não está vazia")
    except deque.DequeVazio():
        print("O Deque está vazio")
    print()
    print()

    deque.delete_first()
    deque.delete_last()

    print('Show: ', end=' ')
    deque.show()
    print('First: ', deque.first())
    print('Last: ', deque.last())
    print('Tamanho: ', len(deque))
    print('Size: ', deque.size())
    print()
    print()

    deque.delete_first()
    deque.delete_last()

    print('Show: ', end=' ')
    deque.show()
    print('First: ', deque.first())
    print('Last: ', deque.last())
    print('Tamanho: ', len(deque))
    print('Size: ', deque.size())
