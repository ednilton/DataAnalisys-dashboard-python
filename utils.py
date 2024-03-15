from dataset import df
import pandas as pd


def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'


## 1 - DataFrame Receita por Estado ##
df_receita_estado = df.groupby('Local da compra')[['Preço']].sum()
# Remove dados duplicados da coluna Local da compra
df_receita_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_receita_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
#print(df_receita_estado)

## 2 - DataFrame Receita Mensal ##
df_receita_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
df_receita_mensal['Ano'] = df_receita_mensal['Data da Compra'].dt.year
df_receita_mensal['Mes'] = df_receita_mensal['Data da Compra'].dt.month_name(locale="Portuguese")

#print(df_receita_mensal)