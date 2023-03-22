import tkinter as tk
import api.__init__ as API
import ui.__init__ as UI

root = tk.Tk()
root.title("Datos a importar")

opciones_departamento = ["AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLANTICO", "BOGOTA", "BOLIVAR", "BOYACA", "CALDAS", "CAQUETA", "CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA", "CUNDINAMARCA", "GUAINIA", "GUAJIRA", "GUAVIARE", "HUILA", "MAGDALENA", "META", "NARIÑO", "NORTE SANTANDER", "PUTUMAYO", "QUINDIO", "RISARALDA", "SANTANDER", "SUCRE", "TOLIMA", "VALLE", "VAUPES", "VICHADA", "STA MARTA D.E."]
variable_departamento = tk.StringVar(root)
variable_departamento.set(opciones_departamento[0])

UI.menu_desplegable(root, opciones_departamento, variable_departamento)
UI.boton_datos(root, API.obtener_datos, UI.campo_limite(root), variable_departamento, UI.campo_resultados(root))

root.mainloop()


