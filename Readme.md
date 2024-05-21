# Estimativa da Taxa de Juros (Selic) por Regressão Linear Simples

Este projeto utiliza regressão linear simples para estimar a taxa de juros Selic em função da taxa de inflação (IPCA) no Brasil, utilizando dados de 2019 a 2020.

## Bibliotecas Utilizadas

- `pandas`: Manipulação de dados
- `numpy`: Operações matemáticas
- `matplotlib`: Visualização de dados
- `statsmodels`: Regressão linear e análise estatística
- `pyettj`: Captura de dados das curvas de juros da B3

## Descrição do Script

1. **Captura de Dados**:
   - A função `fetch_ipca_data` obtém dados da inflação (IPCA) do Banco Central do Brasil.
   - A função `fetch_selic_data` obtém dados da taxa de juros Selic da B3 utilizando a biblioteca `pyettj`.

2. **Análise de Dados**:
   - Os dados de IPCA e Selic são combinados em um único DataFrame.
   - Realiza-se uma regressão linear simples utilizando a biblioteca `statsmodels`.

3. **Visualização**:
   - Um gráfico de dispersão dos dados reais e a linha de regressão estimada é gerado.

## Resultados da Regressão

Após a execução do script, o resumo da regressão linear é apresentado, incluindo:

### Equação da Regressão

Selic=β 
0
​
 +β 
1
​
 ×IPCA

Onde:
- β 
0
​
  é o intercepto.
- β 
1
​
  é o coeficiente da inflação (IPCA).

### Estatísticas do Modelo

- **R-quadrado (R²)**: Indica a proporção da variabilidade na taxa Selic explicada pela inflação (IPCA). Varia de 0 a 1. Um valor próximo de 1 indica um bom ajuste do modelo aos dados.
- **R-quadrado Ajustado**: Similar ao R², mas ajusta para o número de preditores no modelo. É útil para comparar modelos com diferentes números de preditores.
- **Teste t**: Avalia se os coeficientes das variáveis são significativamente diferentes de zero. Um valor absoluto maior indica maior significância.
- **p-valor**: Indica a probabilidade de obter o resultado observado (ou mais extremo) se a hipótese nula for verdadeira. Um p-valor menor que 0.05 geralmente indica significância estatística.

### Interpretação dos Resultados

- **R-quadrado e R-quadrado Ajustado**:
  - Valores próximos de 1 indicam que a inflação (IPCA) explica bem a variabilidade da taxa Selic.
  - Valores baixos sugerem que outros fatores não considerados no modelo podem estar influenciando a taxa Selic.
- **Coeficientes da Regressão**:
  - O intercepto  (
𝛽
0
​
 ) representa a taxa Selic estimada quando a inflação é zero.
  - O coeficiente do IPCA  (
𝛽
1
​
 ) indica a variação esperada na taxa Selic para cada unidade de aumento na inflação.
- **Teste t e p-valores**:
  - Coeficientes com valores de teste t elevados e p-valores menores que 0.05 são considerados estatisticamente significativos, indicando que a inflação tem um impacto significativo na taxa Selic.

## Exemplo de Saída

```plaintext
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  Selic   R-squared:                       0.85
Model:                            OLS   Adj. R-squared:                  0.84
Method:                 Least Squares   F-statistic:                     150.5
Date:                Mon, 20 May 2024   Prob (F-statistic):           3.57e-15
Time:                        12:34:56   Log-Likelihood:                -45.678
No. Observations:                  24   AIC:                             95.36
Df Residuals:                      22   BIC:                             97.58
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          2.3456      0.456      5.143      0.000       1.403       3.288
IPCA           1.7890      0.146     12.271      0.000       1.488       2.090
==============================================================================
Omnibus:                        1.002   Durbin-Watson:                   2.043
Prob(Omnibus):                  0.605   Jarque-Bera (JB):                0.880
Skew:                           0.015   Prob(JB):                        0.643
Kurtosis:                       2.048   Cond. No.                         2.45
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
