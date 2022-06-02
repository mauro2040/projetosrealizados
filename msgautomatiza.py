import pandas as pd

contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)

from selenium import webdriver
from selenium.webdriver.common.keys import keys

navegador = webdriver.chrome()
navegador.get("")