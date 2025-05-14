import time

import allure
import pytest_check as check
from selenium import webdriver

from locators.locators_aliens_page import AliensPage
from page.elements import WebElement

@allure.story('Тест для проверки страницы aliens')
@allure.feature('Тест для проверки блока с ссылками на ресурсы по категории aliens')
def test_check_resource_link(web_browser):
    page = AliensPage(web_browser)

    TEST_LIST_ARTICLE = [
        page. aliens_page_article_link_category_first,
        page. aliens_page_article_link_category_second,
        page. aliens_page_article_link_category_third,
        page. aliens_page_article_link_category_four,
        page. aliens_page_article_link_category_fifth,
        page. aliens_page_article_link_category_six,
        page. aliens_page_article_link_category_seven,
        page. aliens_page_article_link_category_eight,
    ]

    for article in TEST_LIST_ARTICLE:
        WebElement.scroll_to_element(article)
        time.sleep(2)
        category = article.get_text().lower()
        check.is_true('aliens' in category,f'no such category, only:{category}')

@allure.story('Тест для проверки страницы aliens')
@allure.feature('Тест для проверки кнопки, для добавления новых статей по категории aliens')
def test_check_resource_link(web_browser):
    page = AliensPage(web_browser)
    TEST_LIST_ARTICLE = [
        page.aliens_page_article_link_category_first,
        page.aliens_page_article_link_category_second,
        page.aliens_page_article_link_category_third,
        page.aliens_page_article_link_category_four,
        page.aliens_page_article_link_category_fifth,
        page.aliens_page_article_link_category_six,
        page.aliens_page_article_link_category_seven,
        page.aliens_page_article_link_category_eight,
    ]
    WebElement.scroll_to_element(page. aliens_page_btn_add_more)
    time.sleep(2)
    page. aliens_page_btn_add_more.click()
    time.sleep(2)

    for article in TEST_LIST_ARTICLE:
        WebElement.scroll_to_element(article)
        time.sleep(2)
        category = article.get_text().lower()
        check.is_true('aliens' in category, f'no such category, only:{category}')
