from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()


    # говорим WebDriver ждать все элементы в течение 12 секунд
    # browser.implicitly_wait(12)

    browser.get(link)


    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element(By.ID, 'book')
    button.click()


    input4 = browser.find_element(By.ID, 'input_value')
    x = input4.text
    y = calc(x)


    input3 = browser.find_element(By.ID, 'answer')
    input3.send_keys(y)


    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла