#logica de programação
# 1 percorrer todos os arquivos da pasta base de dados(pasta vendas)
from IPython.display import display
import pandas as pd
import os

pasta_vendas = "C:\\Users\\vinic\\Downloads\\01-15 - Curso de Python - Aula 1\\Vendas"
lista_arquivos = os.listdir(pasta_vendas)

tabela_total = pd.DataFrame()
# Importar as bases de dados de vendas
for arquivo in lista_arquivos:
    caminho_arquivo = os.path.join(pasta_vendas, arquivo)
    tabela = pd.read_csv(caminho_arquivo)
    tabela_total=tabela_total._append(tabela)

    

# 3 tratar compilar as bases de dados
display(tabela_total)
# 4 calcular o produto mais vendido (quantidade) 
# 5 calcular o produto que mais faturou
# 6 calcular a loja/cidade que mais faturou - grafico