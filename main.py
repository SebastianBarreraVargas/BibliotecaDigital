# main.py
import tkinter as tk
from view import mostrar_pantalla_principal

def main():
    root = tk.Tk()
    root.title("Biblioteca Online")
    root.geometry("800x550")
    root.configure(bg="white")
    root.resizable(False, False)
    mostrar_pantalla_principal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
