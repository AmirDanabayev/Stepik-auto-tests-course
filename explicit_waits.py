from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    button = WebDriverWait(browser, 5).until_not(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text


finally:
    browser.quit()

# Implicit wait(неявное ожидание) - его не надо явно указывать каждый раз, используется для ожидания прогрузки страницы.
# Explicit Waits(явное ожидание) - позволяют задать специальное ожидание для конкретного элемента.Например, кнопка
# стала кликабельной или кнопка становится неактивной после отправки данных.

