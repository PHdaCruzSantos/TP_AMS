import tkinter as tk
from tkinter import ttk
from plot import carregar_grafo, plotar_grafo_partido, plotar_grafo_comparacao

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

    # Carregar partidos disponíveis
    _, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
    partidos = sorted(set(deputados_partidos.values()))

    # Configurar a interface gráfica
    root = tk.Tk()
    root.title("Visualizador de Grafos por Partido")

    # Frame para análise de um único partido
    frame_partido = tk.Frame(root)
    frame_partido.pack(pady=20)

    label_partido = tk.Label(frame_partido, text="Selecione um partido para analisar:")
    label_partido.pack(pady=10)

    combobox_partido = ttk.Combobox(frame_partido, values=partidos)
    combobox_partido.pack(pady=10)

    button_visualizar = tk.Button(frame_partido, text="Visualizar Grafo", command=on_button_click)
    button_visualizar.pack(pady=10)

    # Frame para comparação de dois partidos
    frame_comparacao = tk.Frame(root)
    frame_comparacao.pack(pady=20)

    label_comparacao = tk.Label(frame_comparacao, text="Comparação entre dois partidos:")
    label_comparacao.pack(pady=10)

    label_partido1 = tk.Label(frame_comparacao, text="Selecione o primeiro partido:")
    label_partido1.pack(pady=10)

    combobox_partido1 = ttk.Combobox(frame_comparacao, values=partidos)
    combobox_partido1.pack(pady=10)

    label_partido2 = tk.Label(frame_comparacao, text="Selecione o segundo partido:")
    label_partido2.pack(pady=10)

    combobox_partido2 = ttk.Combobox(frame_comparacao, values=partidos)
    combobox_partido2.pack(pady=10)

    button_comparar = tk.Button(frame_comparacao, text="Comparar Partidos", command=on_compare_button_click)
    button_comparar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    from index import main_index
    main_index()  # Executa a parte de indexação para obter os dados e gerar os arquivos
    main()  # Executa a interface gráfica
