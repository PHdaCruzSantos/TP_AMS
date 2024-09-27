import networkx as nx

def calcular_centralidade_grau(grafo):
    centralidade = nx.degree_centrality(grafo)
    for deputado, valor in centralidade.items():
        print(f"Deputado: {deputado}, Centralidade de Grau: {valor}")
    return centralidade
