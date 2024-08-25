import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página do Streamlit
st.set_page_config(layout="wide")

# Título e cabeçalho do dashboard
st.title("Curso de Biblioteconomia e Documentação")
st.header("Dashboard do Curso de Biblioteconomia e Documentação")

# Carregar o arquivo CSV
df = pd.read_csv('curso.csv')

# Supondo que a carga horária total para cada semestre seja a soma das CH por status
df['CH_Pendente'] = df.groupby('Semestre')['CH'].transform(lambda x: x[df['Status'] != 'Concluído'].sum())
df['CH_Total'] = df.groupby('Semestre')['CH'].transform('sum')
df['CH_Concluída'] = df['CH_Total'] - df['CH_Pendente']

# Criação dos gráficos
col1, col2 = st.columns(2)

# Gráfico 1: Média de Nota por Semestre com cores
fig_notas = px.bar(df,
                   x="Semestre",
                   y="Nota",
                   color="Nota",
                   title="Média de Nota por Semestre",
                   color_continuous_scale=px.colors.sequential.Viridis)
col1.plotly_chart(fig_notas)

# Gráfico 2: Distribuição do Status das Disciplinas
fig_andamento = px.pie(df,
                       names="Status",
                       title="Distribuição do Status das Disciplinas")
col2.plotly_chart(fig_andamento)

# Gráfico 3: Carga Horária por Semestre e Status (largura total)
fig_ch = px.bar(df,
                x='Semestre',
                y='CH',
                color='Status',
                title='Carga Horária por Semestre e Status',
                barmode='stack')
st.plotly_chart(fig_ch, use_container_width=True)
