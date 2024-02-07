#logica de programação
# 1 percorrer todos os arquivos da pasta base de dados(pasta vendas)

import os
lista_arquivos = os.listdir("C:\\Users\\vinic\Downloads\\01-15 - Curso de Python - Aula 1\\Vendas")

print(lista_arquivos)
# 2 importar as bases de dados de vendas
 
for arquivo in lista_arquivos:
    print(f"C:\\Users\\vinic\Downloads\\01-15 - Curso de Python - Aula 1\\Vendas{arquivo}")

# 3 tratar compilar as bases de dados
# 4 calcular o produto mais vendido (quantidade) 
# 5 calcular o produto que mais faturou
# 6 calcular a loja/cidade que mais faturou - grafico