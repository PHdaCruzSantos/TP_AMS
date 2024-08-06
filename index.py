import requests
import networkx as nx

# Criação do grafo usando a biblioteca networkx
grafo = nx.Graph()
deputados_partidos = {}

def obter_dados_votacoes_por_evento(evento_id):
    url = f"https://dadosabertos.camara.leg.br/api/v2/votacoes/{evento_id}/votos"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = resposta.json()['dados']
        
        if dados:
            for dado in dados:
                deputado_nome = str(dado['deputado_']['nome']).replace(" ", "_")
                partido = dado['deputado_']['siglaPartido']
                deputados_partidos[deputado_nome] = partido
                for dado2 in dados:
                    if dado != dado2 and dado['tipoVoto'] == dado2['tipoVoto'] and dado['deputado_']['nome'] != dado2['deputado_']['nome']:
                        dep1 = deputado_nome
                        dep2 = str(dado2['deputado_']['nome']).replace(" ", "_")
                        if grafo.has_edge(dep1, dep2):
                            grafo[dep1][dep2]['weight'] += 1
                        else:
                            grafo.add_edge(dep1, dep2, weight=1)
        return grafo
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição dos eventos: {e}")
        return []

def id_votacoes():
    url = "https://dadosabertos.camara.leg.br/api/v2/votacoes"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = resposta.json()['dados']
        id_votacoes = []

        if dados:
            for voto in dados:
                id_votacao = voto['id']
                id_votacoes.append(id_votacao)
            return id_votacoes 
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição dos eventos: {e}")
        return []  

def write_dep_votes():
    with open("deputados_votos.txt", 'w') as file:
        for node, degree in grafo.degree():
            file.write(f"{node} {degree}\n")

def write_graph_file():
    with open("grafo_arq.txt", 'w') as file:
        file.write(f"{grafo.number_of_nodes()} {grafo.number_of_edges()}\n")
        for (node1, node2, weight) in grafo.edges(data='weight'):
            file.write(f"{node1} {node2} {weight}\n")
    with open("deputados_partidos.txt", 'w') as file:
        for deputado, partido in deputados_partidos.items():
            file.write(f"{deputado} {partido}\n")

def main_index():
    ids = id_votacoes()
    for id_votacao in ids:
        obter_dados_votacoes_por_evento(id_votacao)
    
    write_dep_votes()
    write_graph_file()
