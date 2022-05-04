from tkinter import *

# Instancia do objeto
menu_inicial = Tk()

# Titulo da janela
menu_inicial.title("Primeiro app")

# Função de evento Botao
def click_print():
    print("Olá comedor")

# Botão
btn = Button(menu_inicial, text = "Executar" , command=click_print)
btn.pack()

# Tamanho definivel
menu_inicial.geometry("500x500+200+200")

# Icone do programa
menu_inicial.iconbitmap("images/icon.ico")

# Proibição para aumentar ou diminuir
menu_inicial.resizable(True, False)

# Máximo de alteração de altura e largura
menu_inicial.maxsize(750, 400)
# Minímo de alteração de Altura e Largura
menu_inicial.minsize(500, 250)

# Loop
menu_inicial.mainloop()