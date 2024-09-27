import networkx as nx

def calcular_assortatividade_partido(grafo, deputados_partidos):
    # Adicionar o atributo "partido" a cada nó
    for node in grafo.nodes:
        grafo.nodes[node]['partido'] = deputados_partidos[node]
    
    # Calcular o coeficiente de assortatividade
    assortatividade = nx.attribute_assortativity_coefficient(grafo, 'partido')
    
    print(f"Assortatividade por Partido: {assortatividade}")
    return assortatividade
