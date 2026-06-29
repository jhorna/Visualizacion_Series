import streamlit as st

st.title("Gráfica de series de tiempo")

entrada = st.text_input("Ingrese la serie, separada por comas:", value="10,15,18,26,31")

try:
    # Convierte los strings a números
    serie = [float(x.strip()) for x in entrada.split(",")]
    
    # Selecciona el tipo de gráfica
    tipo = st.selectbox("Tipo de gráfica:", ["Línea", "Área", "Barras"])
    
    if tipo == "Línea":
        st.line_chart(serie)
    elif tipo == "Área":
        st.area_chart(serie)
    else:
        st.bar_chart(serie)
        
except ValueError:
    st.error("❌ Error: Ingresa números separados por comas (ej: 10,15,18,26,31)")
