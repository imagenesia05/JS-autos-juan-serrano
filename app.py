import streamlit as st
import pandas as pd

st.set_page_config(page_title="Autos Juan Serrano", page_icon=":car:", layout="centered")

st.image("logo.png", width=200)
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
        resultado = resultado[resultado.get("Precio", pd.Series([0]*len(resultado))) <= int(palabra)]
    else:
        resultado = resultado[resultado.apply(lambda fila: palabra in str(fila).lower(), axis=1)]

# Mostrar resultados
if not resultado.empty:
    for _, fila in resultado.iterrows():
        st.subheader(f"{fila.get('Marca', 'No disponible')} {fila.get('Modelo', '')} ({fila.get('Año', '')})")
        st.write(f"**Tipo:** {fila.get('Tipo', 'No disponible')}")
        st.write(f"**Transmisión:** {fila.get('Transmisión', 'No disponible')}")
        st.write(f"**Color:** {fila.get('Color', 'No disponible')}")
        st.write(f"**Precio:** ${fila.get('Precio', 'No disponible')}")
        st.image(fila.get('Foto', ''), width=300)
        st.markdown("---")
else:
    st.warning("No se encontraron vehículos que coincidan con tu búsqueda.")
