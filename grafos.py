# from pprint import pprint

# Como identificar ciclos ?
# V= passos ou perguntas
# Arestas= proximo asso ou resposta
# Algoritmo para identificar um ciclo em um grafo --->
# busca em profundidade (dfs)


class Vertice:
    def __init__(self, rotulo: str) -> None:
        self.rotulo = rotulo
        self.right: Vertice | None = None
        self.left: Vertice | None = None

    def __repr__(self) -> str:
        return self.rotulo


class Grapho:
    def __init__(self) -> None:
        self.grafo: list[Vertice] = []
        self.lista_adjacencia: dict[str, list[Vertice]] = {}

    def add_vertice(self, vertice: Vertice):
        self.grafo.append(vertice)
        self.lista_adjacencia[vertice.rotulo] = []

    def add_aresta_direcionada(self, vertice_primeiro: Vertice,
                               vertice_segundo: Vertice,
                               direcao: str):

        self.lista_adjacencia[vertice_primeiro.rotulo].append(vertice_segundo)

        if (direcao == 'r'):
            vertice_primeiro.right = vertice_segundo
        elif (direcao == 'l'):
            vertice_primeiro.left = vertice_segundo
        elif (direcao == 's'):
            vertice_primeiro.right = vertice_primeiro


a = Vertice('a')
b = Grapho()
b.add_vertice(a)
print(b.grafo)


# class Grafo:
#     '''
#     Representação de grafos em python
#     '''

#     def __init__(self, vertices: int) -> None:
#         self.vertices = vertices
#         self.rotulos_vertices = str([n for n in range(1, self.vertices + 1)])
#         self.grafo = [[0]*self.vertices for _ in range(self.vertices)]
#         self.arestas = 0

#     def add_aresta(self, u: int, v: int):
#         if u - 1 < len(self.grafo) and v - 1 < len(self.grafo) and (
#                 self.grafo[u-1][v-1] == 0) and u != v:

#             self.grafo[u-1][v-1] = -1
#             self.grafo[v-1][u-1] = 1
#             self.arestas += 1

#         else:
#             print("Já possui a ligação ou Não existe no grafo")

#     def delete_aresta(self, u: int, v: int):
#         if u - 1 < len(self.grafo) and v - 1 < len(self.grafo):
#             self.grafo[u-1][v-1] = 0
#             self.arestas -= 1

#         else:
#             print("Já retirou a ligação ou Não existe no grafo")


# grafo = Grafo(5)
# grafo.add_aresta(1, 2)
# grafo.add_aresta(1, 3)
# grafo.add_aresta(2, 4)
# grafo.add_aresta(2, 5)

# pprint(grafo.grafo)
