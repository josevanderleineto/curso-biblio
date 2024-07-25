import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Curso de Bibliteconomia e Documentação")
st.header("Dashboard do curso de Bibliteconomia e Documentação")
df = pd.read_csv('curso.csv')
df

col1, col2 = st.columns(2)

fig_notas = px.bar(df,
                   x="Semestre",
                   y="CH",
                   color="Nota",
                   title="Media de nota por semestre")
col1.plotly_chart(fig_notas)

fig_andamento = px.pie(df,
                       names="Status",
                       title="Distribuição do Status das Disciplinas")
col2.plotly_chart(fig_andamento)

fig_ch = px.bar(df,
                x='Semestre',
                y='CH',
                color='Status',
                title='Carga Horária por Semestre e Status',
                barmode='stack')
st.plotly_chart(fig_ch)
