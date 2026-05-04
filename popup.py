import customtkinter as ctk
import random
from screeninfo import get_monitors

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

estudiantes = [
    "MARIA SUAREZ",
    "CAMILO ARTEAGA",
    "ALEJANDRO ROMERO",
    "JOSE DAVID ARTEAGA",
    "JUAN DAVID ARTEAGA",
    "DANIEL MARIN",
]

offset_x = 0
offset_y = 0


def iniciar_arrastre(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def mover_ventana(event):
    x = root.winfo_pointerx() - offset_x
    y = root.winfo_pointery() - offset_y
    root.geometry(f"+{x}+{y}")

def elegir():
    label.configure(text=random.choice(estudiantes))

def limpiar():
    label.configure(text="")

def cerrar():
    root.destroy()

def posicionar_ventana(root, ancho=300, alto=140):
    monitores = get_monitors()

    monitor = monitores[1] if len(monitores) > 1 else monitores[0]

    x = monitor.x + 20
    y = monitor.y + 20

    root.geometry(f"{ancho}x{alto}+{x}+{y}")

# 🔹 Ventana principal
root = ctk.CTk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.bind("<Button-1>", iniciar_arrastre)
root.bind("<B1-Motion>", mover_ventana)

# 🔹 Contenedor principal (con bordes redondeados visuales)
frame = ctk.CTkFrame(root, corner_radius=15)
frame.pack(fill="both", expand=True, padx=5, pady=5)

# 🔹 Header
header = ctk.CTkFrame(frame, fg_color="transparent")
header.pack(fill="x", padx=10, pady=(10, 5))

btn_elegir = ctk.CTkButton(
    header,
    text="🎯 Escoger",
    command=elegir,
    width=100,
    corner_radius=10
)
btn_elegir.pack(side="left", padx=5)

btn_limpiar = ctk.CTkButton(
    header,
    text="🧹 Limpiar",
    command=limpiar,
    width=100,
    corner_radius=10,
    fg_color="#444"
)
btn_limpiar.pack(side="left", padx=5)

btn_cerrar = ctk.CTkButton(
    header,
    text="✖",
    command=cerrar,
    width=40,
    corner_radius=10,
    fg_color="#d32f2f",
    hover_color="#b71c1c"
)
btn_cerrar.pack(side="right", padx=5)

# 🔹 Label resultado
label = ctk.CTkLabel(
    frame,
    text="",
    font=("Segoe UI", 14, "bold"),
    wraplength=260,
    justify="center"
)
label.pack(expand=True, padx=10, pady=10)

posicionar_ventana(root)

root.mainloop()