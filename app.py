import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

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
    
    # Calcular línea de tendencia y proyección
    X = np.array(range(len(serie))).reshape(-1, 1)
    y = np.array(serie)
    
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    # Proyectar 6 períodos futuros
    X_futuro = np.array(range(len(serie), len(serie) + 6)).reshape(-1, 1)
    y_futuro = modelo.predict(X_futuro)
    
    # Crear gráfica con Plotly
    fig = go.Figure()
    
    # Datos originales
    fig.add_trace(go.Scatter(
        x=list(range(len(serie))),
        y=serie,
        mode='lines+markers',
        name='Datos reales',
        line=dict(color='blue', width=2),
        marker=dict(size=8)
    ))
    
    # Línea de tendencia histórica
    y_tendencia = modelo.predict(X)
    fig.add_trace(go.Scatter(
        x=list(range(len(serie))),
        y=y_tendencia,
        mode='lines',
        name='Tendencia',
        line=dict(color='orange', width=2, dash='dash')
    ))
    
    # Proyección futura
    fig.add_trace(go.Scatter(
        x=list(range(len(serie)-1, len(serie) + 6)),
        y=list([serie[-1]]) + list(y_futuro),
        mode='lines+markers',
        name='Proyección (6 períodos)',
        line=dict(color='red', width=2, dash='dot'),
        marker=dict(size=6)
    ))
    
    # Diseño
    fig.update_layout(
        title="Serie de tiempo con tendencia y proyección",
        xaxis_title="Período",
        yaxis_title="Valor",
        hovermode='x unified',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar tabla de datos
    st.subheader("📊 Tabla de datos")
    df = pd.DataFrame({
        "Índice": range(len(serie)),
        "Valor": serie
    })
    st.dataframe(df, use_container_width=True)
    
    # Mostrar proyecciones
    st.subheader("🔮 Proyecciones para los próximos 6 períodos")
    df_proyecciones = pd.DataFrame({
        "Período": range(len(serie), len(serie) + 6),
        "Valor proyectado": [f"{v:.2f}" for v in y_futuro]
    })
    st.dataframe(df_proyecciones, use_container_width=True)
        
except ValueError:
    st.error("❌ Error: Ingresa números separados por comas (ej: 10,15,18,26,31)")