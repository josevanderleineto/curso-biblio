import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página do Streamlit
st.set_page_config(layout="wide")

# Título e cabeçalho do dashboard
st.title("Curso de Biblioteconomia e Documentação")
st.header("Dashboard do Curso de Biblioteconomia e Documentação")

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('curso.db')
query = "SELECT * FROM curso"
df = pd.read_sql_query(query, conn)
conn.close()

# Mostrando o DataFrame
st.dataframe(df)

# Criação dos gráficos
col1, col2 = st.columns(2)

fig_notas = px.bar(df,
                   x="Semestre",
                   y="CH",
                   color="Nota",
                   title="Média de Nota por Semestre")
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
