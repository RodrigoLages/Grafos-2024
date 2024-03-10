from ast import Return
from pprint import pprint
from tabnanny import verbose

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
        self.pai: Vertice | None = None
        self.tempos = [0, 0]

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

TEMPO = 0

def dfs_verification(V: Vertice, G: Grapho):
    global TEMPO
    V.verificado += 1 # Vertice descoberto
    TEMPO += 1
    V.tempos[0] = TEMPO

    # Checa se á um vertice não descoberto adjacente
    for adj in G.lista_adjacencia[V.rotulo]:
        if adj.verificado == 0:
            adj.pai = V
            dfs_verification(adj, G) # Caso tenha, atualiza o pai e visita

    # Termina de visitar o vertice 
    V.verificado += 1
    TEMPO += 1
    V.tempos[1] = TEMPO


def dfs(G: Grapho):
    global TEMPO
    TEMPO = 0

    print(G.lista_adjacencia)

    for t, vertice in enumerate(G.vertices):
        if vertice.verificado == 0:
            dfs_verification(vertice, G)

    for v in G.vertices:
        print(v.rotulo)
        print("pai: ", v.pai)
        print(v.tempos)


dfs(grafo)