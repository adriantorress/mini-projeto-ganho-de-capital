class FilaVazia(Exception):
    pass


class FilaArray:
    def __init__(self, capacidade=10, dados=None):
        if dados == None:
            self._dados = [None] * capacidade
            self._tamanho = 0
        else:
            self._dados = dados
            self._tamanho = len(dados)
        self._inicio = 0

    def __len__(self):
        return self._tamanho

    def fila_to_list(self):
        lista = []
        posicao = self._inicio
        for k in range(self._tamanho):
            lista.append(self._dados[posicao])
            posicao = (1 + posicao) % len(self._dados)
        return lista

    def size(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0

    def first(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        return self._dados[self._inicio]

    def dequeue(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        if 0 < self._tamanho <= (len(self._dados) // 4):
            self._altera_tamanho(len(self._dados) // 2)
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result

    def enqueue(self, e):
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
        result = "Ações: ["
        for k in range(self._tamanho):
            if k == (self._tamanho-1):
                result += str(self._dados[posicao])
            else:
                result += str(self._dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self._dados)
        result += f'] Quantidade: {len(self)}\n'
        return result


if __name__ == "__main__":
    fila = FilaArray()
    fila.enqueue(5)
    fila.enqueue(2)
    fila.enqueue(3)
    fila.enqueue(10)
    fila.enqueue(8)
    fila.enqueue(7)
    fila.enqueue(1)
    fila.enqueue(0)
    fila.enqueue(4)
    fila.enqueue(6)
    fila.show()
    print(fila.first())
    print()
    fila.enqueue(11)
    print(fila)
    fila.dequeue()
    fila.dequeue()
    fila.dequeue()
    fila.dequeue()
    fila.dequeue()
    fila.dequeue()
    fila.dequeue()
    print(fila)
    fila.dequeue()
    fila.dequeue()
    fila.dequeue()
    fila.dequeue()
    print(fila)
