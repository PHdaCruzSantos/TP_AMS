import networkx as nx

def gerar_grafo_interpartido(grafo, deputados_partidos):
    subgrafo = nx.Graph()

    # Iterar sobre todas as arestas do grafo original
    for source, target, data in grafo.edges(data=True):
        # Se os deputados são de partidos diferentes, adicionar a conexão
        if deputados_partidos[source] != deputados_partidos[target]:
            subgrafo.add_edge(source, target, weight=data['weight'])
    
    return subgrafo

def gerar_subgrafo_comparacao_interpartido(grafo, deputados_partidos, partido1, partido2):
  subgrafo = nx.Graph()

  # Iterar sobre todas as arestas do grafo original
  for source, target, data in grafo.edges(data=True):
      # Conectar apenas deputados de partidos diferentes entre partido1 e partido2
      if (deputados_partidos[source] == partido1 and deputados_partidos[target] == partido2) or \
          (deputados_partidos[source] == partido2 and deputados_partidos[target] == partido1):
          subgrafo.add_edge(source, target, weight=data['weight'])
  
  return subgrafo