import streamlit as st
import pandas as pd

st.set_page_config(page_title="Autos Juan Serrano", page_icon=":car:", layout="centered")

st.image("https://i.imgur.com/ZQy7AIw.png", width=150)
st.title("Autos Juan Serrano")

st.write("Bienvenido al catálogo en línea de Autos Juan Serrano. Utiliza el buscador para encontrar el vehículo ideal para ti.")

# Cargar datos desde Google Sheets (CSV)
sheet_url = "https://docs.google.com/spreadsheets/d/1b1Cae-Qo1Rjc4BKt7riThTPprXKRrFvkpeNnKgjpVq4/export?format=csv"
data = pd.read_csv(sheet_url)

# Buscador
busqueda = st.text_input("¿Qué auto estás buscando? (Ej: SUV Toyota blanco 20000)").lower().split()

# Filtrar
resultado = data.copy()
for palabra in busqueda:
    if palabra.isdigit():
        resultado = resultado[resultado["Precio"] <= int(palabra)]
    else:
        resultado = resultado[resultado.apply(lambda fila: palabra in str(fila).lower(), axis=1)]

# Mostrar resultados
if not resultado.empty:
    for _, fila in resultado.iterrows():
        st.subheader(f"{fila['Marca']} {fila['Modelo']} ({fila['Año']})")
        st.write(f"**Tipo:** {fila['Tipo']}")
        st.write(f"**Transmisión:** {fila['Transmisión']}")
        st.write(f"**Color:** {fila['Color']}")
        st.write(f"**Precio:** ${fila['Precio']}")
        st.image(fila['Foto'], width=300)
        st.markdown("---")
else:
    st.warning("No se encontraron vehículos que coincidan con la búsqueda.")
