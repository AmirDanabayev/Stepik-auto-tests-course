from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    priceCriteria = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    bookButton = browser.find_element_by_id("book").click()

    # проскроллить страницу до заголовка с задачей
    h3 = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", h3)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    # print(x)
    y = calc(x)

    answerField = browser.find_element_by_id("answer").send_keys(y)

    # говорим Selenium проверять в течение 5 секунд пока кнопка станет активной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    button.click()

finally:
    time.sleep(10)
    browser.quit()

