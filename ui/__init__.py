import tkinter as tk

def menu_desplegable(root, opciones_departamento, variable_departamento):
    # Crear el menú desplegable
    opcion_departamento = tk.OptionMenu(root, variable_departamento, *opciones_departamento)
    opcion_departamento.pack()

def campo_limite(root):
    # Crear los campos de entrada
    limite_label = tk.Label(root, text='Escriba el límite de registros (máximo 1000):')
    limite_label.pack()
    limite_entry = tk.Entry(root)
    limite_entry.pack()

    return limite_entry

def boton_datos(root, obtener_datos, limite_entry, variable_departamento, resultado_text):
    # Crear el botón para obtener los datos
    def obtener():
        limite_registros = limite_entry.get()
        nombre_departamento = variable_departamento.get()
        resultados = obtener_datos(limite_registros, nombre_departamento)
        resultado_text.delete('1.0', tk.END)
        resultado_text.insert(tk.END, resultados.to_string(index=False))

    obtener_datos_boton = tk.Button(root, text='Obtener datos', command=obtener)
    obtener_datos_boton.pack()

def campo_resultados(root):
    # Crear un campo de texto para mostrar los resultados
    resultado_label = tk.Label(root, text='Resultados:')
    resultado_label.pack()
    resultado_text = tk.Text(root)
    resultado_text.pack()

    return resultado_text
