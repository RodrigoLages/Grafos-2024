from pprint import pprint

# Como identificar ciclos ?
# V= passos ou perguntas
# Arestas= proximo asso ou resposta
# Algoritmo para identificar um ciclo em um grafo --->
# busca em profundidade (dfs)


class Vertice:
    '''
        Represntação de vértice em python
    '''

    def __init__(self, rotulo: str) -> None:
        self.rotulo = rotulo
        self.right: Vertice | None = None
        self.left: Vertice | None = None

    def __repr__(self) -> str:
        return self.rotulo


class Grapho:
    '''
        Represntação de grafo em python
    '''

    def __init__(self) -> None:
        self.grafo: list[Vertice] = []
        self.lista_adjacencia: dict[str, list[Vertice]] = {}

    def add_vertice(self, vertice: Vertice):
        '''
            Adicionando vértices ao grafos
        '''
        self.grafo.append(vertice)
        self.lista_adjacencia[vertice.rotulo] = []

    def add_aresta_direcionada(self, vertice_primeiro: Vertice,
                               vertice_segundo: Vertice,
                               direcao: str = ''):
        '''
            Criando as ligações (arestas) entre vértices
        '''

        if vertice_segundo not in (
                self.lista_adjacencia[vertice_primeiro.rotulo]):

            self.lista_adjacencia[vertice_primeiro.rotulo].append(
                vertice_segundo)

            if (direcao == 'r'):
                vertice_primeiro.right = vertice_segundo
            elif (direcao == 'l'):
                vertice_primeiro.left = vertice_segundo
            elif (direcao == '' and vertice_primeiro == vertice_segundo):
                vertice_primeiro.right = vertice_primeiro

            return self.lista_adjacencia


a = Vertice('A')
b = Vertice('B')
c = Vertice('C')

grafo = Grapho()
grafo.add_vertice(a)
grafo.add_vertice(b)
grafo.add_vertice(c)
grafo.add_aresta_direcionada(a, b, 'l')
grafo.add_aresta_direcionada(a, a)
grafo.add_aresta_direcionada(a, b, 'l')
grafo.add_aresta_direcionada(c, a, 'l')

pprint(grafo.lista_adjacencia)
