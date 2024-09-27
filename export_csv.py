import csv
from grafo_interpartido import gerar_grafo_interpartido

def exportar_grafo_para_gephi(grafo, deputados_partidos):
    # Exportar os nós (nodes.csv)
    with open('nodes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Label', 'Partido'])  # Cabeçalho do CSV
        for node in grafo.nodes():
            writer.writerow([node, node.replace("_", " "), deputados_partidos[node]])  # Id e nome do deputado

    # Exportar as arestas (edges.csv)
    with open('edges.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Source', 'Target', 'Weight'])  # Cabeçalho do CSV
        for source, target, data in grafo.edges(data=True):
            writer.writerow([source, target, data['weight']])  # Deputados conectados e o peso da conexão

def export_grafo_interpartido(grafo, deputados_partidos):
    subgrafo = gerar_grafo_interpartido(grafo, deputados_partidos)

    # Exportar os nós (nodes.csv)
    with open('nodes_interpartidario.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Label', 'Partido'])  # Cabeçalho do CSV
        for node in subgrafo.nodes():
            writer.writerow([node, node.replace("_", " "), deputados_partidos[node]])  # Id e nome do deputado

    # Exportar as arestas (edges.csv)
    with open('edges_interpartidario.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Source', 'Target', 'Weight'])  # Cabeçalho do CSV
        for source, target, data in subgrafo.edges(data=True):
            writer.writerow([source, target, data['weight']])  # Deputados conectados e o peso da conexão

    print("Arquivos nodes_interpartidario.csv e edges_interpartidario.csv gerados com sucesso!")
