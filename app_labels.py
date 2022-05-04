from cProfile import label
from tkinter import *

# Instancia do objeto
menu_inicial = Tk()

# Titulo da janela
menu_inicial.title("Primeiro app")

# Label 
label_1 = Label(menu_inicial, text= "Este é meu Label 1")
label_2 = Label(menu_inicial, text= "Este é meu Label 2")
cmd = Button(menu_inicial, text="Executar")
# Pack
cmd.pack()
label_1.pack()
label_2.pack()

# Loop
menu_inicial.mainloop()