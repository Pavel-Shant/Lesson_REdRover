# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))
# print("Сумма чисел а+б =", a + b)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_footer_elements(browser):
    # Открываем главную страницу
    browser.get("https://only.digital/")

    # Ожидаем загрузки футера
    footer = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )

    # Проверяем основные элементы футера
    elements_to_check = {
        "Логотип": (By.CSS_SELECTOR, "footer .footer__logo"),
        "Телефон": (By.CSS_SELECTOR, "footer .footer-contacts__phone"),
        "Email": (By.CSS_SELECTOR, "footer .footer-contacts__email"),
        "Соцсети": (By.CSS_SELECTOR, "footer .social-links"),
        "Копирайт": (By.CSS_SELECTOR, "footer .footer__copyright")
    }

    for element_name, locator in elements_to_check.items():
        element = footer.find_element(*locator)
        assert element.is_displayed(), f"{element_name} не отображается в футере"
        print(f"Элемент {element_name} найден")

    # Дополнительная проверка количества ссылок в соцсетях
    social_links = footer.find_elements(By.CSS_SELECTOR, ".social-links a")
    assert len(social_links) >= 3, "Меньше 3 социальных ссылок в футере"


if __name__ == "__main__":
    pytest.main(["-v", "-s"])