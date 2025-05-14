import time

import allure
import pytest_check as check
from selenium import webdriver

from locators.locators_press_page import PressPage
from page.elements import WebElement

@allure.story('Тест для проверки страницы прессы')
@allure.feature('Тест для проверки блока с ссылками на ресурсы под блоком с информацией о издании')
def test_check_resource_link(web_browser):
    page = PressPage(web_browser)

    RESOURCE_LINKS = [
        # page. press_link_further_information,
        # page. press_link_facebook,
        page. press_link_main_page,
        page. press_link_instagram,
        page. press_link_twitter,
        page. press_link_youtube,
    ]

    for element in RESOURCE_LINKS:
        WebElement.scroll_to_element(element)
        time.sleep(2)
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(element.is_visible(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(element.is_clickable(), f'{element.get_text()}')