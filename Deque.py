class DequeVazio(Exception):
    pass


class DequeArray:
    def __init__(self, capacidade=10):
        self._dados = [None] * capacidade
        self._tamanho = 0
        self._inicio = 0
        self._final = 0

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
        return self._dados[self._final]

    def delete_first(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        if 0 < self._tamanho < len(self._dados) // 4:
            self._aumenta_tamanho(len(self._dados) // 2)
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result

    def delete_last(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        if 0 < self._tamanho < len(self._dados) // 4:
            self._aumenta_tamanho(len(self._dados) // 2)
        result = self._dados[self._final]
        self._dados[self._final] = None
        self._final = (self._final - 1) % len(self._dados)
        self._tamanho -= 1
        return result

    def add_first(self, e):
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))
        disponivel = (self._final + self._tamanho) % len(self._dados)
        self._dados[disponivel] = e
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
            result += str(self._dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self._dados)
        result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
        return result
