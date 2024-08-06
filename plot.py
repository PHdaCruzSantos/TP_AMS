import networkx as nx
import matplotlib.pyplot as plt

def carregar_grafo(nome_arquivo_grafo, nome_arquivo_partidos):
    grafo = nx.Graph()
    deputados_partidos = {}
    
    with open(nome_arquivo_partidos, 'r') as file:
        for line in file:
            deputado, partido = line.strip().split()
            deputados_partidos[deputado] = partido
    
    with open(nome_arquivo_grafo, 'r') as file:
        lines = file.readlines()
        n_nodes, n_edges = map(int, lines[0].strip().split())
        for line in lines[1:]:
            node1, node2, weight = line.strip().split()
            grafo.add_edge(node1, node2, weight=int(weight))
    
    return grafo, deputados_partidos

def plotar_grafo(grafo, deputados_partidos):
    # Define cores para cada partido
    cores_partidos = {partido: idx for idx, partido in enumerate(set(deputados_partidos.values()))}
    cores_nos = [cores_partidos[deputados_partidos[node]] for node in grafo.nodes]
    
    pos = nx.spring_layout(grafo)  # Posição dos nós
    
    plt.figure(figsize=(12, 12))
    nx.draw(grafo, pos, node_color=cores_nos, with_labels=True, node_size=500, cmap=plt.cm.tab20)
    plt.show()

def plotar_grafo_partido(grafo, deputados_partidos, partido_selecionado):
    subgrafo = nx.Graph()
    for node in grafo.nodes:
        if deputados_partidos[node] == partido_selecionado:
            subgrafo.add_node(node)
            for neighbor in grafo.neighbors(node):
                if deputados_partidos[neighbor] == partido_selecionado:
                    subgrafo.add_edge(node, neighbor, weight=grafo[node][neighbor]['weight'])
    
    pos = nx.spring_layout(subgrafo, k=0.15, iterations=20)  # Ajustar layout para melhor visualização
    plt.figure(figsize=(14, 14))
    edges = subgrafo.edges(data=True)
    
    # Desenhar nós e arestas
    nx.draw_networkx_nodes(subgrafo, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(subgrafo, pos, edgelist=edges, width=0.5, edge_color='gray')

    # Adicionar etiquetas aos nós
    nx.draw_networkx_labels(subgrafo, pos, font_size=10, font_family='sans-serif')

    # Adicionar pesos das arestas como etiquetas
    edge_labels = {(u, v): d['weight'] for u, v, d in edges}
    nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=edge_labels, font_size=8)
    
    plt.title(f"Grafo do Partido: {partido_selecionado}")
    plt.show()

def main_plot():
    # Carrega o grafo e os partidos
    grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")

    # Plota o grafo
    plotar_grafo(grafo, deputados_partidos)
