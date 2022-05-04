from tkinter import *

# Instancia do objeto
menu_inicial = Tk()

# Titulo da janela
menu_inicial.title("Primeiro app")

# Dimensoes da janela
largura = 500
altura = 300

# Resolução do nosso sistema
largura_screen = menu_inicial.winfo_screenmmwidth()
altura_screen = menu_inicial.winfo_screenmmheight()

# Posição da janela
posx = largura/2 - largura_screen/2
posy = altura/2 - altura_screen/2 
print(posx, posy)

# Definir a geometry
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

menu_inicial.mainloop()