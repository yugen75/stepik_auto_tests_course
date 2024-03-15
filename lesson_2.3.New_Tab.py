from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "*.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input4 = browser.find_element(By.ID, 'input_value')
    x = input4.text
    y = calc(x)

    input3 = browser.find_element(By.ID, 'answer')
    input3.send_keys(y)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла