from cProfile import label
from tkinter import *

# Instancia do objeto
menu_inicial = Tk()

# Titulo da janela
menu_inicial.title("Primeiro app")
# menu_inicial.geometry("500x500")

# Labels
label1 = Label(menu_inicial, text =" Label1", bg="red", font="Arial 20")
label2 = Label(menu_inicial, text =" Label2", bg="green", font="Arial 20")
label3 = Label(menu_inicial, text =" Label3", bg="yellow", font="Arial 20")

# Botões
btn1 = Button(menu_inicial, text="Click1")
btn2 = Button(menu_inicial, text="Click2")
btn3 = Button(menu_inicial, text="Click3")
# Label grid
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)

# Botões grid
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)

# Loop
menu_inicial.mainloop()