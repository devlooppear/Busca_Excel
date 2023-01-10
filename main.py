import pandas as pd

CONDICAO = 55000

def nomes_arquivos_xlsx():
    lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',]
    return lista_meses

def busca(lista_meses):
    for mes in lista_meses:
        tabela_vendas = pd.read_excel(f"{mes}.xlsx")
        if (tabela_vendas['Vendas'] > CONDICAO).any():
            vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > CONDICAO, 'Vendedor'].values[0]
            vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > CONDICAO, 'Vendas'].values[0]
            print(f"No mês {mes} foi encontrado alguém com mais de {CONDICAO}. Vendedor {vendedor}, com as vendas {vendas}")

def main():
    lista_meses = nomes_arquivos_xlsx()
    busca(lista_meses)

main()