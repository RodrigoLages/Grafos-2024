from ast import Return
from pprint import pprint
from tabnanny import verbose

from pymysql import TIME

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
        self.verificado: int = 0
        self.right: Vertice | None = None
        self.left: Vertice | None = None

    def __repr__(self) -> str:
        return self.rotulo


class Grapho:
    '''
        Represntação de grafo em python
    '''

    def __init__(self) -> None:
        # Lista dos vértices
        self.vertices: list[Vertice] = []

        # Apenas uma representação visual do grafo com seus vértices e arestas
        self.lista_adjacencia: dict[str, list[Vertice]] = {}

    def add_vertice(self, vertice: Vertice):
        '''
            Adicionando vértices ao grafos
        '''
        self.vertices.append(vertice)
        self.lista_adjacencia[vertice.rotulo] = []

    def add_aresta_direcionada(self, vertice_primeiro: Vertice,
                               vertice_segundo: Vertice):
        '''
            Criando as ligações (arestas) entre vértices
        '''

        if vertice_segundo not in (
                self.lista_adjacencia[vertice_primeiro.rotulo]):

            self.lista_adjacencia[vertice_primeiro.rotulo].append(
                vertice_segundo)

            if vertice_primeiro.right is None:
                vertice_primeiro.right = vertice_segundo
            else:
                vertice_primeiro.left = vertice_segundo

            return self.lista_adjacencia


u = Vertice('U')
v = Vertice('V')
w = Vertice('W')
x = Vertice('X')
y = Vertice('Y')
z = Vertice('Z')

grafo = Grapho()
grafo.add_vertice(u)
grafo.add_vertice(v)
grafo.add_vertice(w)
grafo.add_vertice(x)
grafo.add_vertice(y)
grafo.add_vertice(z)

grafo.add_aresta_direcionada(u, v)
grafo.add_aresta_direcionada(u, x)
grafo.add_aresta_direcionada(v, y)
grafo.add_aresta_direcionada(w, y)
grafo.add_aresta_direcionada(w, z)
grafo.add_aresta_direcionada(x, v)
grafo.add_aresta_direcionada(y, x)
grafo.add_aresta_direcionada(z, z)


def dfs_verification(V: Vertice, TIMES: list[list[int]], PAIS: list, t: int):
    V.verificado += 1
    TIMES[t][0] += t + 1


def dfs(G: Grapho):
    QUANTIDADE = len(G.vertices)
    pais = [None for _ in range(QUANTIDADE)]
    tempos = [[0, 0] for _ in range(QUANTIDADE)]

    print(G.lista_adjacencia)

    for t, vertice in enumerate(G.vertices):
        dfs_verification(vertice, tempos, pais, t)

    print(pais)
    print(tempos)


dfs(grafo)
