import streamlit as st
import pandas as pd

st.title("Gráfica de series de tiempo")

entrada = st.text_input("Ingrese la serie, separada por comas:", value="10,15,18,26,31")

try:
    serie = [float(x.strip()) for x in entrada.split(",")]
    
    # Mostrar estadísticas
    col1, col2, col3 = st.columns(3)
    col1.metric("Promedio", f"{sum(serie)/len(serie):.2f}")
    col2.metric("Máximo", max(serie))
    col3.metric("Mínimo", min(serie))
    
    # Selecciona el tipo de gráfica
    tipo = st.selectbox("Tipo de gráfica:", ["Línea", "Área", "Barras"])
    
    if tipo == "Línea":
        st.line_chart(serie)
    elif tipo == "Área":
        st.area_chart(serie)
    else:
        st.bar_chart(serie)
    
    # Mostrar tabla de datos
    st.subheader("📊 Tabla de datos")
    df = pd.DataFrame({
        "Índice": range(len(serie)),
        "Valor": serie
    })
    st.dataframe(df, use_container_width=True)
        
except ValueError:
    st.error("❌ Error: Ingresa números separados por comas (ej: 10,15,18,26,31)")