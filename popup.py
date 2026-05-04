import tkinter as tk
import random
from screeninfo import get_monitors


estudiantes = [
    "MARIA SUAREZ",
    "CAMILO ARTEAGA",
    "ALEJANDRO ROMERO",
]

def elegir():
    label.config(text=random.choice(estudiantes))

def limpiar():
    label.config(text="")

def cerrar():
    root.destroy()

def posicionar_ventana(root, ancho=260, alto=120):
    monitores = get_monitors()

    # Si hay más de un monitor → usa el secundario
    if len(monitores) > 1:
        monitor = monitores[1]
    else:
        monitor = monitores[0]

    # Posición: esquina inferior derecha del monitor elegido
    x = monitor.x + 20
    y = monitor.y + 20

    root.geometry(f"{ancho}x{alto}+{x}+{y}")

root = tk.Tk()

# Siempre encima
root.attributes("-topmost", True)

# Sin bordes
root.overrideredirect(True)

# Tamaño y posición
root.geometry("260x120+50+50")

# Fondo
root.configure(bg="black")

# 🔹 Cabecera
header = tk.Frame(root, bg="black")
header.pack(fill="x")

btn_elegir = tk.Button(header, text="Escoger", command=elegir)
btn_elegir.pack(side="left", padx=5, pady=5)

btn_limpiar = tk.Button(header, text="Limpiar", command=limpiar)
btn_limpiar.pack(side="left", padx=5, pady=5)

btn_cerrar = tk.Button(header, text="✖", command=cerrar, bg="red", fg="white")
btn_cerrar.pack(side="right", padx=5, pady=5)

# 🔹 Resultado
label = tk.Label(
    root,
    text="",
    fg="white",
    bg="black",
    font=("Arial", 10),
    wraplength=240,
    justify="center"
)
label.pack(expand=True)

posicionar_ventana(root)

root.mainloop()