from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir Google
driver.get("https://www.google.com")

# Buscar "calculadora"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("calculadora")
search_box.send_keys(Keys.RETURN)

time.sleep(2)  # Esperar que se cargue la página

# Realizar una operación
result_box = driver.find_element(By.XPATH, "//div[@class='result']/div[1]/span")
print("El resultado es:", result_box.text)

# Cerrar el navegador
driver.quit()
