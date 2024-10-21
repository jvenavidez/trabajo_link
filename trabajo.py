from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controlador = webdriver.Chrome()
controlador.maximize_window()

controlador.get("https://web.facebook.com/?locale=es_LA&_rdc=1&_rdr")
time.sleep(1)

usuario = controlador.find_element(By.NAME, "email")
clave = controlador.find_element(By.NAME, "pass")
olvidastecontra=controlador.find_element(By.LINK_TEXT,"https://web.facebook.com/recover/initiate/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzI5NTI4Nzg5LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&ars=facebook_login&next")
usuario.send_keys("dfpachon")
clave.send_keys("12345678910")

time.sleep(1)

boton = controlador.find_element(By.CLASS_NAME, "btn-primaryy")
boton.click()

time.sleep(2)
controlador.quit()