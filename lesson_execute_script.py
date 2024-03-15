from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input4 = browser.find_element(By.ID, 'input_value')
    x = input4.text
    y = calc(x)

    input3 = browser.find_element(By.ID, 'answer')
    input3.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()

    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла