import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

st.set_page_config(layout='wide')

st.header('Acompanhamento do Comportamento de Compra')

df = pd.read_csv('data/cluster_customer.csv')

st.sidebar.header('Filtros')
clusters_options = df['cluster'].unique() if 'cluster' in df.columns else []
selected_clusters = st.sidebar.multiselect('Clusters', clusters_options)

if not selected_clusters:
    selected_clusters = clusters_options

df = df[df['cluster'].isin(selected_clusters)]


# Quantidade de Clientes por grupo
clientes_por_grupo = df['cluster'].value_counts().reset_index()
clientes_por_grupo.columns = ['Clusters', 'Quantidade de Clientes']
fig1 = px.bar(clientes_por_grupo, x='Clusters', y='Quantidade de Clientes', title='Quantidade de Clientes por Grupo')

# Média de Faturamento por grupo
faturamento_por_grupo = df.groupby('cluster')['Spent'].mean().reset_index()
faturamento_por_grupo.columns = ['Clusters', 'Faturamento Médio']
fig2 = px.bar(faturamento_por_grupo, x='Clusters', y='Faturamento Médio', title='Faturamento Médio por Grupo')

# Recência Média por Grupo
recencia_por_grupo = df.groupby('cluster')['Recency'].mean().reset_index()
recencia_por_grupo.columns = ['Clusters', 'Recencia Média']
fig3 = px.bar(recencia_por_grupo, x='Clusters', y='Recencia Média', title='Recencia Média por Grupo')


# Idade Média por Grupo
idade_por_grupo = df.groupby('cluster')['Age'].mean().reset_index()
idade_por_grupo.columns = ['Clusters', 'Idade Média']
fig4 = px.bar(idade_por_grupo, x='Clusters', y='Idade Média', title='Idade Média por Grupo')

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
with col2:
    st.plotly_chart(fig3, use_container_width=True)
    st.plotly_chart(fig4, use_container_width=True)

df = df.dropna(subset=['Spent'])

df = df.dropna(subset=['Spent'])

color_palette = px.colors.qualitative.Set3  # Opções: Set1, Set2, Set3, Dark2, etc.

# Criar o gráfico de dispersão com a paleta personalizada
fig = px.scatter(
    df,
    x="embedding_x",
    y="embedding_y",
    color="cluster",
    size="Spent",
    color_continuous_scale='Viridis',
    title="Análise de Clusters",
)

# Ajustar as dimensões
fig.update_layout(height=800, width=1000)

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)




st.dataframe(df)