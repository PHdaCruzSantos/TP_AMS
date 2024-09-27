import tkinter as tk
from tkinter import ttk
import networkx as nx
from plot import carregar_grafo, plotar_grafo_partido, plotar_grafo_comparacao, plotar_grafo
from degree_centrality import calcular_centralidade_grau
from betweenness_centrality import calcular_centralidade_intermediacao
from export_csv import exportar_grafo_para_gephi, export_grafo_interpartido
from grafo_interpartido import gerar_grafo_interpartido, gerar_subgrafo_comparacao_interpartido
def main():
    def on_button_click():
        partido_selecionado = combobox_partido.get()
        if partido_selecionado:
            grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
            plotar_grafo_partido(grafo, deputados_partidos, partido_selecionado)

    def on_compare_button_click():
        partido1 = combobox_partido1.get()
        partido2 = combobox_partido2.get()
        if partido1 and partido2:
            grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
            plotar_grafo_comparacao(grafo, deputados_partidos, partido1, partido2)

    def exibir_resultados(titulo, dados):
        """Função para exibir os resultados de uma forma mais clara e estilizada."""
        resultados_window = tk.Toplevel(root)
        resultados_window.title(titulo)
        resultados_window.geometry("500x400")

        # Adicionar um estilo
        style = ttk.Style(resultados_window)
        style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'))
        style.configure("Treeview", font=('Helvetica', 10))

        tree = ttk.Treeview(resultados_window, columns=("deputado", "valor"), show='headings')
        tree.heading("deputado", text="Deputado")
        tree.heading("valor", text="Valor")
        
        # Formatação dos dados na tabela
        for deputado, valor in dados.items():
            tree.insert("", tk.END, values=(deputado, f"{valor:.4f}"))

        tree.pack(expand=True, fill='both', padx=20, pady=20)

        # Adicionar barra de rolagem
        scrollbar = ttk.Scrollbar(resultados_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar.set)

    def on_centralidade_grau_click():
        partido_selecionado = combobox_partido.get()
        if partido_selecionado:
            grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
            subgrafo = nx.Graph()
            for node in grafo.nodes:
                if deputados_partidos[node] == partido_selecionado:
                    subgrafo.add_node(node)
                    for neighbor in grafo.neighbors(node):
                        if deputados_partidos[neighbor] == partido_selecionado:
                            subgrafo.add_edge(node, neighbor, weight=grafo[node][neighbor]['weight'])
            
            # Calcular centralidade de grau
            centralidades = calcular_centralidade_grau(subgrafo)

            # Exibir os resultados em formato de tabela
            exibir_resultados(f"Centralidade de Grau - {partido_selecionado}", centralidades)

            # Plotar o grafo do partido
            plotar_grafo_partido(grafo, deputados_partidos, partido_selecionado)

    def on_centralidade_intermediacao_click():
        partido_selecionado = combobox_partido.get()
        if partido_selecionado:
            grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
            subgrafo = nx.Graph()
            for node in grafo.nodes:
                if deputados_partidos[node] == partido_selecionado:
                    subgrafo.add_node(node)
                    for neighbor in grafo.neighbors(node):
                        if deputados_partidos[neighbor] == partido_selecionado:
                            subgrafo.add_edge(node, neighbor, weight=grafo[node][neighbor]['weight'])
            
            # Calcular centralidade de intermediação
            centralidades = calcular_centralidade_intermediacao(subgrafo)

            # Exibir os resultados em formato de tabela
            exibir_resultados(f"Centralidade de Intermediação - {partido_selecionado}", centralidades)

            # Plotar o grafo do partido
            plotar_grafo_partido(grafo, deputados_partidos, partido_selecionado)

    def on_subgrafo_interpartidario_click():
        # Carregar grafo completo
        grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
        
        # Gerar subgrafo entre partidos
        subgrafo = gerar_grafo_interpartido(grafo, deputados_partidos)
        
        # Plotar o subgrafo interpartidário
        plotar_grafo(subgrafo, deputados_partidos)

        # Exportar subgrafo para o formato CSV (Gephi)
        export_grafo_interpartido(subgrafo, deputados_partidos)

    def on_comparacao_interpartidaria_click():
        partido1 = combobox_partido1.get()
        partido2 = combobox_partido2.get()
        if partido1 and partido2:
            # Carregar o grafo completo
            grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
            
            # Gerar subgrafo de comparação entre partidos
            subgrafo = gerar_subgrafo_comparacao_interpartido(grafo, deputados_partidos, partido1, partido2)
            # exportar_subgrafo_comparacao_partidos_para_gephi(grafo, deputados_partidos, partido1, partido2)

            plotar_grafo_comparacao(subgrafo, deputados_partidos, partido1, partido2)
            

    
    # Carregar partidos disponíveis
    _, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
    partidos = sorted(set(deputados_partidos.values()))

   # Configurar a interface gráfica com abas
    root = tk.Tk()
    root.title("Visualizador de Grafos por Partido")
    root.geometry("700x600")

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)

    # Aba para análise de um único partido
    frame_partido = ttk.Frame(notebook)
    notebook.add(frame_partido, text="Análise por Partido")

    label_partido = ttk.Label(frame_partido, text="Selecione um partido:")
    label_partido.pack(pady=10)

    combobox_partido = ttk.Combobox(frame_partido, values=partidos)
    combobox_partido.pack(pady=10)

    button_visualizar = ttk.Button(frame_partido, text="Visualizar Grafo", command=on_button_click)
    button_visualizar.pack(pady=10)

    button_centralidade_grau = ttk.Button(frame_partido, text="Centralidade de Grau", command=on_centralidade_grau_click)
    button_centralidade_grau.pack(pady=10)

    button_centralidade_intermediacao = ttk.Button(frame_partido, text="Centralidade de Intermediação", command=on_centralidade_intermediacao_click)
    button_centralidade_intermediacao.pack(pady=10)


    # Aba para análise interpartidária
    frame_interpartidario = ttk.Frame(notebook)
    notebook.add(frame_interpartidario, text="Análise Interpartidária")

    button_exportar_subgrafo = ttk.Button(frame_interpartidario, text="Exportar Subgrafo Interpartidário", command=on_subgrafo_interpartidario_click)
    button_exportar_subgrafo.pack(pady=20)

    # Aba para comparação entre partidos
    frame_comparacao = ttk.Frame(notebook)
    notebook.add(frame_comparacao, text="Comparação entre Partidos")

    label_partido1 = ttk.Label(frame_comparacao, text="Selecione o primeiro partido:")
    label_partido1.pack(pady=10)

    combobox_partido1 = ttk.Combobox(frame_comparacao, values=partidos)
    combobox_partido1.pack(pady=10)

    label_partido2 = ttk.Label(frame_comparacao, text="Selecione o segundo partido:")
    label_partido2.pack(pady=10)

    combobox_partido2 = ttk.Combobox(frame_comparacao, values=partidos)
    combobox_partido2.pack(pady=10)

    button_comparar = ttk.Button(frame_comparacao, text="Comparar Partidos", command=on_compare_button_click)
    button_comparar.pack(pady=10)

    button_comparacao_interpartidaria = ttk.Button(frame_comparacao, text="Comparação Interpartidária", command=on_comparacao_interpartidaria_click)
    button_comparacao_interpartidaria.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    from index import main_index
    main_index()  # Executa a parte de indexação para obter os dados e gerar os arquivos
    main()  # Executa a interface gráfica