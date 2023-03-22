import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)

def obtener_datos(limite_registros, nombre_departamento):
    # Recuperar los datos de la API
    results = client.get("gt2j-8ykr", where=f"departamento_nom = '{nombre_departamento}'", limit=int(limite_registros))
    results_df = pd.DataFrame.from_records(results)

    # Seleccionar las columnas que se desean mostrar
    columns_to_show = ['ciudad_municipio_nom', 'departamento_nom', 'sexo', 'edad', 'estado']
    results_df = results_df[columns_to_show]

    return results_df