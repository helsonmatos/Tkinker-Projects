from cProfile import label
from tkinter import *

# Instancia do objeto
menu_inicial = Tk()

# Titulo da janela
menu_inicial.title("Primeiro app")
menu_inicial.geometry("500x500")

# Label 
label1 = Label(menu_inicial)
label1['text'] = "texto_teste"
label1['font'] = "consola"
label1['bd'] = 1
label1['relief'] = "solid"
label1.pack()

# Loop
menu_inicial.mainloop()