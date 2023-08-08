# código de geração do gráfico 
import pandas as pd
import seaborn as sns

dados_gasolina = pd.read_csv('dolar.csv')

with sns.axes_style('darkgrid'):
  grafico_dolar = sns.lineplot(
      x = 'dia',
      y = 'venda',
      data = dados_dolar
  )
  
  grafico_dolar.set(
      title = 'cotação do dolar nos ultimos dez dias',
      xlabel = 'Dia',
      ylabel = 'Preço (R$)'
  )
  
  figura = grafico_dolar.get_figure()    
  figura.savefig('dolar.png', dpi=600)
