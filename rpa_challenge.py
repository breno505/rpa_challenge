from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

navegador = webdriver.Firefox()
navegador.get("https://www.rpachallenge.com/")

botao_start = navegador.find_element(By.XPATH, "//button[text()='Start']")
botao_start.click()

planilha = pd.read_excel("challenge.xlsx")

for index, row in planilha.iterrows():

    email = navegador.find_element(By.XPATH,"//input[@ng-reflect-name='labelEmail']").send_keys(row['Email'])
    first_name = navegador.find_element(By.XPATH,"//input[@ng-reflect-name='labelFirstName']").send_keys(row['First Name'])
    last_name = navegador.find_element(By.XPATH,"//input[@ng-reflect-name='labelLastName']").send_keys(row['Last Name '])
    address = navegador.find_element(By.XPATH,"//input[@ng-reflect-name='labelAddress']").send_keys(row['Address'])
    phone_number = navegador.find_element(By.XPATH,"//input[@ng-reflect-name='labelPhone']").send_keys(row['Phone Number'])
    role_in_company = navegador.find_element(By.XPATH,"//input[@ng-reflect-name='labelRole']").send_keys(row['Role in Company'])
    company_name = navegador.find_element(By.XPATH,"//input[@ng-reflect-name='labelCompanyName']").send_keys(row['Company Name'])

    botao_submit = navegador.find_element(By.XPATH, "//input[@type='submit']")
    botao_submit.click()






time.sleep(3)
#navegador.close()