import streamlit as st

st.title("Grafica de series de tiempo")

entrada = st.text_input("Ingrese la serie, separada por comas:", value="10,15,18,26,31")

try:
    # Convierte los strings a números
    serie = [float(x.strip()) for x in entrada.split(",")]
    
    st.line_chart(serie)
except ValueError:
    st.error("❌ Error: Ingresa números separados por comas (ej: 10,15,18,26,31)")