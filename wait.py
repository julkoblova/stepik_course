from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector("#book")
    button.click()
    
    # Ищем значение в поле input_value и преобразуем в инт
    bord = browser.find_element_by_css_selector("#input_value")
    x = int(bord.text)
    z = calc(x)

    # Вставляем найденное значение в найденное поле
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(z)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
