from tkinter import *

# Instancia do objeto
menu_inicial = Tk()

# Titulo da janela
menu_inicial.title("Primeiro app")

# Tamanho definivel
menu_inicial.geometry("500x500+200+200")

menu_inicial.iconbitmap("images/icon.ico")

# Proibição para aumentar ou diminuir
menu_inicial.resizable(True, False)

# Máximo de alteração de altura e largura
menu_inicial.maxsize(750, 400)
# Minímo de alteração de Altura e Largura
menu_inicial.minsize(500, 250)

menu_inicial.mainloop()