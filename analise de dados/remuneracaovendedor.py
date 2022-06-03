
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC782d6ecb496cfa66e9de39340f5308f9"
# Your Auth Token from twilio.com/console
auth_token  = "c9e722a9b4d6633460821bf32fb37d3a"
client = Client(account_sid, auth_token)
lista_meses= ["janeiro","fevereiro","fevereiro","março","abril","maio","junho"]

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f"No mês {mes} foi batida a meta + 55 mil, o valor foi {vendas}, e o vendedor foi {vendedor}")
        message = client.messages.create(
            to="+5519994149901",
            from_="+12484222863",
            body=f"No mês {mes} foi batida a meta + 55 mil, o valor foi {vendas}, e o vendedor foi {vendedor}")
        print(message.sid)

#Passo a passo da solução
#Abrir 6 arquivos
#Verificar se algumvalor coluna venda > 55 mil
#Se for + que 55 mil, enviar SMS com o nome o mês e as vendas
#Caso nao seja maior que 55 mil, não fazer nada