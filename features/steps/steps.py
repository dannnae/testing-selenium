from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

CHROME_DRIVER_PATH = 'C:\\chromedriver\\chromedriver.exe'  

service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

@given('que puedo acceder a la página Sence')
def step_impl(context):
    print("Iniciando ChromeDriver...")
    service = Service(executable_path=CHROME_DRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    print("Abriendo la página de Sence...")
    context.driver.get('https://www.sence.cl')
    context.driver.maximize_window()

@when('puedo acceder al login')
def step_impl(context):
    print("Buscando botón de login...")
    login_button = context.driver.find_element(By.LINK_TEXT, 'Iniciar sesión')  # Asegúrate de que este selector sea correcto
    login_button.click()

@when('ingreso a Clave Única')
def step_impl(context):
    print("Ingresando a Clave Única...")
    clave_unica_button = context.driver.find_element(By.LINK_TEXT, 'Clave Única')  # Ajusta el selector
    clave_unica_button.click()

@when('ingreso los datos correspondientes')
def step_impl(context):
    print("Ingresando datos de usuario...")
    username_field = context.driver.find_element(By.ID, 'username')  # Ajusta el selector
    password_field = context.driver.find_element(By.ID, 'password')  # Ajusta el selector
    username_field.send_keys('tu_usuario')  # Reemplaza con los datos correspondientes
    password_field.send_keys('tu_contraseña')  # Reemplaza con los datos correspondientes

@when('realizo el envío de los datos')
def step_impl(context):
    print("Enviando datos...")
    submit_button = context.driver.find_element(By.ID, 'submit')  # Ajusta el selector
    submit_button.click()

@then('aparece un mensaje de ingreso correcto')
def step_impl(context):
    print("Verificando mensaje de ingreso correcto...")
    time.sleep(5)  # Espera para que cargue la página
    success_message = context.driver.find_element(By.XPATH, '//*[contains(text(), "Ingreso correcto")]')  # Ajusta el selector
    assert success_message is not None, "El mensaje de ingreso correcto no apareció"
    context.driver.quit()
