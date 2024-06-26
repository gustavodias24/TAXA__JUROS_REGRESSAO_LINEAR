import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pyettj.ettj as ettj
import datetime


# Função para buscar dados da inflação (IPCA) html5lib
def fetch_ipca_data(start_year, end_year):
    ipca_url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/{start_year}&dataFinal=31/12/{end_year}'
    ipca_data = pd.read_csv(ipca_url, sep=';', parse_dates=['data'])
    ipca_data.rename(columns={'data': 'Date', 'valor': 'IPCA'}, inplace=True)
    ipca_data['IPCA'] = ipca_data['IPCA'].str.replace(',', '.').astype(
        float)  # Converter vírgulas para pontos e depois para float
    return ipca_data


# Parâmetros
start_year = 2019
end_year = 2020

# Buscar dados
ipca_data = fetch_ipca_data(start_year, end_year)
selic_data = ettj.get_ettj('02/01/2019')  # Função para buscar dados da taxa Selic

# faça um script em python para estimar a taxa de juros (Selic) por regressão linear simples usando a função Taxa de Juros (Selic) em relação à Inflação (IPCA)(Selic em função da taxa de inflação - IPCA)
# Unir dados em um único DataFrame
# Regressão Linear
# Resultados da Regressão
# Visualizar resultados

# # Unir dados em um único DataFrame
# data = pd.merge(ipca_data, selic_data, on='Date', how='inner')
#
# # Regressão Linear
# X = data['IPCA']
# Y = data['Selic']
# X = sm.add_constant(X)  # Adicionar constante para o termo de interceptação
#
# model = sm.OLS(Y, X).fit()
# predictions = model.predict(X)
#
# # Resultados da Regressão
# print(model.summary())
#
# # Visualizar resultados
# plt.figure(figsize=(10, 6))
# plt.scatter(data['IPCA'], data['Selic'], color='blue', label='Dados reais')
# plt.plot(data['IPCA'], predictions, color='red', label='Linha de Regressão')
# plt.xlabel('IPCA')
# plt.ylabel('Selic')
# plt.title('Regressão Linear Simples: Selic em função do IPCA')
# plt.legend()
# plt.show()
