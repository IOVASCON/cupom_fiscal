import tkinter as tk

# Cria uma janela simples para testar tkinter
root = tk.Tk()
root.title("Teste Tkinter")
label = tk.Label(root, text="Tkinter está funcionando!")
label.pack()
root.mainloop()
