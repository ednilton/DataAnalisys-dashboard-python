import json
import pandas as pd

file = open('vendas.json')
data = json.load(file)

#print(data)

df = pd.DataFrame.from_dict(data)

#print(df)

# Passando para essa coluna o formato DateTime: dia/mes/ano.
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()