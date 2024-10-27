from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def iniciar_navegador():
    """Inicializa el navegador y devuelve el objeto del controlador."""
    driver = webdriver.Chrome()
    return driver

def buscar_calculadora(driver):
    """Realiza la búsqueda de 'calculadora' en Google."""
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("calculadora")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Esperar a que se cargue la página

def realizar_calculo(driver, operacion):
    """Realiza la operación de cálculo en la calculadora de Google."""
    try:
        # Encuentra la caja de entrada y envía la operación
        input_box = driver.find_element(By.XPATH, "//input[@class='a61j6 Vku8d']")
        input_box.send_keys(operacion)
        input_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Esperar el resultado

        # Obtener y mostrar el resultado
        result_box = driver.find_element(By.XPATH, "//div[@class='BNeawe iBp4i AP7Wnd']")
        print(f"El resultado de {operacion} es: {result_box.text}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    """Función principal para ejecutar el script."""
    driver = iniciar_navegador()
    
    try:
        buscar_calculadora(driver)

        # Aquí puedes cambiar la operación por lo que desees
        operaciones = ["3 + 5", "12 * 4", "9 - 2", "45 / 5", "2 ^ 10"]
        
        for operacion in operaciones:
            realizar_calculo(driver, operacion)
            time.sleep(1)  # Espera entre cálculos

    finally:
        driver.quit()  # Asegúrate de cerrar el navegador

if __name__ == "__main__":
    main()
