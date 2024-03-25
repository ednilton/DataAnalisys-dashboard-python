import plotly.express as px # importa nossa biblioteca gráfica
from utils import df_receita_estado, df_receita_mensal, df_receita_categoria, df_vendedores


grafico_map_receita_estado = px.scatter_geo(
    df_receita_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template  = 'seaborn', 
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado '
)


grafico_receita_mensal = px.line(
    df_receita_mensal,
    x = 'Mes',
    y= 'Preço',
    markers=True,
    range_y=(0, df_receita_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
) 

grafico_receita_mensal.update_layout(yaxis_title = 'Receita')

# head retorna os maiores resultados e tail retorna os 5 menores
grafico_receita_estado = px.bar(
    df_receita_estado.head(10), 
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top Receitas por Estado'
)

# Gráficos de Categorias
grafico_receita_categoria = px.bar(
    df_receita_categoria.head(7),
    text_auto= True,
    title= 'Top 7 Categorias com maior receita'
)

# Gráfico receita vendedores
grafico_receita_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x = 'sum',
    y= df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index, 
    text_auto=True,
    title='Top 76 Vendedores por Receita'
)

# Gráfico de volume de vendas por vendedores
grafico_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count', ascending=False).head(7),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,
    title='Top 7 Vendedores por Venda'
)