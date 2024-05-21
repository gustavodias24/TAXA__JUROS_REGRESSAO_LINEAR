import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pyettj.ettj as ettj


# Função para buscar dados da inflação (IPCA)
def fetch_ipca_data(start_year, end_year):
    ipca_url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/{start_year}&dataFinal=31/12/{end_year}'
    ipca_data = pd.read_csv(ipca_url, sep=';', parse_dates=['data'])
    ipca_data.rename(columns={'data': 'Date', 'valor': 'IPCA'}, inplace=True)
    ipca_data['IPCA'] = ipca_data['IPCA'].str.replace(',', '.').astype(
        float)  # Converter vírgulas para pontos e depois para float
    return ipca_data


# Função para buscar dados selic
def fetch_selic(start_year, end_year):
    datas = ettj.listar_dias_uteis(start_year, end_year)

    todas_datas = pd.DataFrame()
    for dat in datas:
        ano, mes, dia = dat.split("-")
        data = "/".join([dia, mes, ano])
        try:
            dados = ettj.get_ettj(data)
            todas_datas = pd.concat([dados, todas_datas])
        except:
            continue

    return todas_datas.rename(columns={'Data': 'Date'})


# Parâmetros de tempo
start_year = "01/01/2019"
end_year = "01/01/2020"

# Buscar dados
ipca_data = fetch_ipca_data(start_year, end_year)
selic_data = fetch_selic(start_year, end_year)

ipca_data["Date"] = pd.to_datetime(ipca_data["Date"], format='%d/%m/%Y')
selic_data["Date"] = pd.to_datetime(selic_data["Date"], format='%d/%m/%Y')

# Selecionar colunas necessárias de selic_data
selic_data = selic_data[['Date', 'Selic x pré 252']]

# Renomear coluna de Selic para facilitar
selic_data.rename(columns={'Selic x pré 252': 'Selic'}, inplace=True)

# Unir os dados com base na data
data = pd.merge(ipca_data, selic_data, on='Date', how='inner')

# Verificar dados
print(data.head())

# Preparar os dados para regressão polinomial
X = data['IPCA']
y = data['Selic']

# Adicionar termos polinomiais (quadrático)
X_poly = np.column_stack((X, X ** 2))
X_poly = sm.add_constant(X_poly)

# Estimar o modelo de regressão polinomial
model_poly = sm.OLS(y, X_poly).fit()

# Resumo do modelo
print(model_poly.summary())

# Plotar os dados e a curva de regressão polinomial
plt.figure(figsize=(10, 6))
plt.scatter(data['IPCA'], data['Selic'], color='blue', label='Dados observados')

# Gerar valores preditos
x_range = np.linspace(X.min(), X.max(), 100)
x_range_poly = np.column_stack((x_range, x_range ** 2))
x_range_poly = sm.add_constant(x_range_poly)
y_range_pred = model_poly.predict(x_range_poly)

plt.plot(x_range, y_range_pred, color='red', label='Curva de regressão polinomial')
plt.xlabel('Inflação (IPCA)')
plt.ylabel('Taxa de Juros (Selic)')
plt.title('Regressão Polinomial: Selic vs IPCA')
plt.legend()
plt.show()
