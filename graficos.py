import plotly.express as px # importa nossa biblioteca gráfica
from utils import df_receita_estado, df_receita_mensal


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