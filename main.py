import tkinter as tk
from tkinter import ttk
from plot import carregar_grafo, plotar_grafo_partido

def main():
    def on_button_click():
        partido_selecionado = combobox.get()
        if partido_selecionado:
            grafo, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
            plotar_grafo_partido(grafo, deputados_partidos, partido_selecionado)

    # Carregar partidos disponíveis
    _, deputados_partidos = carregar_grafo("grafo_arq.txt", "deputados_partidos.txt")
    partidos = sorted(set(deputados_partidos.values()))

    # Configurar a interface gráfica
    root = tk.Tk()
    root.title("Visualizador de Grafos por Partido")

    label = tk.Label(root, text="Selecione um partido:")
    label.pack(pady=10)

    combobox = ttk.Combobox(root, values=partidos)
    combobox.pack(pady=10)

    button = tk.Button(root, text="Visualizar Grafo", command=on_button_click)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    from index import main_index
    main_index()  # Executa a parte de indexação para obter os dados e gerar os arquivos
    main()  # Executa a interface gráfica
