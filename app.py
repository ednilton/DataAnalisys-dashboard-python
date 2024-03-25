import streamlit as st 
import plotly.express as px # importa nossa biblioteca gráfica
from dataset import  df  # importa o df do nosso arquivo dataset.py
from utils import format_number # importando o aquivo utils e a função para formatar numeros em casas de milhares
from graficos import grafico_map_receita_estado, grafico_receita_mensal, grafico_receita_estado, grafico_receita_categoria, grafico_receita_vendedores, grafico_vendas_vendedores # importa nosso grafico por estado


# Configurando a página no formato landing page
st.set_page_config(layout="wide")

# Adicionando título ao dashboard
st.title("Dashboard de Vendas :shopping_trolley:")

# Criando um SideBar para adicionar Filtros para Vendedores
st.sidebar.title("Filtro de Vendedores")

# Implementando Filtros
filtro_vendedor = st.sidebar._multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

#Adicionando abas para melhorar a visualização dos dados
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

# Enquanto estiver na aba1 execute o df: dataframe que importamos do nosso dataset.py
with aba1:
    st.dataframe(df)

# Na aba2 iremos dividir a tela em duas colunas para exibir nossas métricas
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(grafico_map_receita_estado, use_container_width=True)
        st.plotly_chart(grafico_receita_estado, use_container_width=True)

    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_receita_mensal, use_container_width=True)
        st.plotly_chart(grafico_receita_categoria, use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_receita_vendedores)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores)

    