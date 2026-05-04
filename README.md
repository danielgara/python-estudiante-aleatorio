# 🎲 Selector Aleatorio de Estudiantes (Overlay para Presentaciones)

Pequeña aplicación en Python que muestra un **selector aleatorio de estudiantes** en una ventana flotante, ideal para usar mientras estás en modo presentación en PowerPoint u otro software.

---

## 🚀 Características

* Ventana **siempre visible (always on top)**
* Funciona sobre presentaciones (modo ventana recomendado)
* Selección aleatoria de estudiantes
* Botones:

  * **Escoger** 🎲
  * **Limpiar**
  * **Cerrar**
* Posicionamiento automático en **monitor secundario** (si existe)
* Diseño minimalista tipo widget

---

## 🖥️ Requisitos

* Python 3.8 o superior
* Dependencias:

```bash
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```txt
screeninfo==0.8.1
customtkinter==5.1.3
```

---

## ▶️ Cómo ejecutar

```bash
python popup.py
```

---

## 🧠 Uso en clase (recomendado)

Para mejores resultados con PowerPoint:

1. Abrir la presentación en
   👉 **modo ventana (no pantalla completa exclusiva)**

2. Ejecutar la app

3. Ubicarla en el monitor del profesor

4. Presionar:

   * **Escoger** → selecciona estudiante
   * **Limpiar** → borra resultado

---

## 🧩 Personalización

### ➤ Cambiar lista de estudiantes

Editar el arreglo en el código (en popup.py):

```python
estudiantes = [
    "Nombre Apellido",
    "Otro Estudiante",
]
```

---

### ➤ Cambiar posición

Dentro de la función `posicionar_ventana`:

* Arriba izquierda:

```python
x = monitor.x + 20
y = monitor.y + 20
```

* Abajo derecha:

```python
x = monitor.x + monitor.width - ancho - 20
y = monitor.y + monitor.height - alto - 40
```

---

## ⚠️ Notas

* `tkinter` ya viene incluido con Python (no instalar aparte)
* Si la ventana no aparece encima:

  * Ejecutar después de abrir la presentación
  * Usar modo ventana en PowerPoint

---

## 💡 Ideas para mejorar

* Evitar repetición de estudiantes
* Animación tipo “ruleta”
* Cargar lista desde Excel
* Ventana arrastrable
* Sonidos o efectos visuales

---

## 📄 Licencia

Uso libre para fines educativos y personales.

---

## ✨ Autor

Herramienta pensada para clases dinámicas y participación activa.
