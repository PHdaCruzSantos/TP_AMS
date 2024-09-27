import networkx as nx

def calcular_centralidade_intermediacao(grafo):
    centralidade = nx.betweenness_centrality(grafo)
    for deputado, valor in centralidade.items():
        print(f"Deputado: {deputado}, Centralidade de Intermediação: {valor}")
    return centralidade
