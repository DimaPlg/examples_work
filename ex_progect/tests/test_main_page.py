import time

import allure
import pytest_check as check
from selenium import webdriver

from locators.locators_main_page import MainPage
from page.elements import WebElement


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_main_page_header_btm(web_browser):

    page = MainPage(web_browser)

    HEADER_BTN_CHECK_CLICK = [
        page.btn_header_logo,
        page.headers_gif,
    ]
    for element in HEADER_BTN_CHECK_CLICK:
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(element.is_visible(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(element.is_clickable(), f'{element.get_text()}')

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки конечной ссылки кнопки лого на главной странице')
def test_main_page_logo_btm(web_browser):
    page = MainPage(web_browser)
    page.btn_header_logo.click()
    time.sleep(2)
    check.is_true(page.get_current_url() == 'https://weeklyworldnews.com/', f'Now url {page.get_current_url()}')

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки главного меню')
def test_main_page_header_btm(web_browser):

    page = MainPage(web_browser)

    MAIN_MENU_BTN_CHECK_CLICK = [
        page.main_menu_headliners,
        page.main_menu_free_subscription,
        page.main_menu_shop,
        page.main_menu_aliens,
        page.main_menu_mutants,
        page.main_menu_bat_boy,
        page.main_menu_greatest_people,
        page.main_menu_press,
        page.main_menu_about,
        page.main_menu_youtube_chanel,
        page.main_menu_facebook,
        page.main_menu_instagram,
        page.main_menu_twitter,
    ]
    for element in MAIN_MENU_BTN_CHECK_CLICK:
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(element.is_visible(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(element.is_clickable(), f'{element.get_text()}')


#
# @allure.story('Тест для проверки выпадающих меню')
# @allure.feature('Тест для проверки выпадающих меню на соответствие')
# def test_drop_down_btm(web_browser):
#
#     page = MainPage(web_browser)
#     actions = ActionChains(page)
#     DROP_DOWN_ALIENS = [
#         # (page.main_menu_gootans, 'Gootans', 'https://weeklyworldnews.com/tag/gootans/')
#         # (page.main_menu_zeebans, 'Zeebans', 'https://weeklyworldnews.com/tag/zeebans/')
#         (page.main_menu_ufo_sightings,'UFO Sightings', 'https://weeklyworldnews.com/tag/ufo-sightings/'),
#     ]
#
#     DROP_DOWN_MUTANTS = [
#         # (page.main_menu_mutants_zombies, 'Zombies', 'https://weeklyworldnews.com/tag/zombies/')
#         # (page.main_menu_mutants_bigfoot, 'Bigfoot', 'https://weeklyworldnews.com/tag/bigfoot/')
#         (page.main_menu_mutants_phd_ape,'Phd Ape', 'https://weeklyworldnews.com/tag/phd-ape/'),
#         (page.main_menu_mutants_bat_boy, 'Bat Boy', 'https://weeklyworldnews.com/tag/bat-boy/'),
#         (page.main_menu_mutants_vampires, 'Vampires', 'https://weeklyworldnews.com/tag/vampires/'),
#         (page.main_menu_mutants_manigator, 'Manigator', 'https://weeklyworldnews.com/tag/manigator/'),
#     ]
#
#     DROP_DOWN_ABOUT = [
#         (page.main_menu_contact, 'CONTACT', 'https://weeklyworldnews.com/contact/')
#     ]
#
#     DROP_DOWN_LINKS = [
#         (page.main_menu_aliens, DROP_DOWN_ALIENS),
#         (page.main_menu_mutants, DROP_DOWN_MUTANTS),
#         (page.main_menu_about, DROP_DOWN_ABOUT),
#     ]
#
#
#     for btm_drop_down, elements in DROP_DOWN_LINKS:
#         for element, text_btm, url_btm in elements:
#             element.find()
#             actions.move_to_element(btm_drop_down).perform()
#             check.is_true(element.is_visible(), f'{text_btm} unvisible')
#             actions.move_to_element(element).click().perform()
#             check.is_true(page.get_current_url() == url_btm, f'Now url {page.get_current_url()}')
@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки функции поиска')
def test_main_page_search_funktion(web_browser):

    page = MainPage(web_browser)

    WRONG_REQUEST = 'nothing found'

    REQUESTS= [[page.main_menu_search_bar,page.main_menu_input_search_bar,'a',page.main_page_title,True],
               [page.main_menu_search_bar,page.main_menu_input_search_bar,'dog',page.main_page_title,True],
               [page.main_menu_search_bar,page.main_menu_input_search_bar,'+++',page.main_page_title, False],
               [page.main_menu_search_bar,page.main_menu_input_search_bar,'tiger',page.main_page_title,True]
               ]

    for search_bar,input_line,request,search_result,result_compering_expected_actual in REQUESTS:
        search_bar.click()
        time.sleep(2)
        input_line.send_keys(request + '\n')
        time.sleep(2)

        check.equal(search_result.get_text().lower() != WRONG_REQUEST, result_compering_expected_actual,
                    f'Not expected result search:{input_line}')

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки блока с ссылками на статьи')
def test_main_page_body_links_article(web_browser):

    page = MainPage(web_browser)

    HEADER_BTN_CHECK_CLICK = [
        page.main_page_article_link_first,
        page.main_page_article_link_last,
    ]
    for element in HEADER_BTN_CHECK_CLICK:
        WebElement.scroll_to_element(element)
        time.sleep(2)
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(element.is_visible(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(element.is_clickable(), f'{element.get_text()}')

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки кнопки добавления статей')
def test_main_page_btm_for_more_news(web_browser):

    page = MainPage(web_browser)
    last_article_link = page.main_page_article_link_last
    WebElement.scroll_to_element(last_article_link)
    name_article = last_article_link.get_text().lower()
    time.sleep(2)

    btm = page.main_page_btm_for_more_news
    WebElement.scroll_to_element(btm)
    time.sleep(2)
    btm.click()

    last_article_link = page.main_page_article_link_last
    WebElement.scroll_to_element(last_article_link)
    time.sleep(2)
    check.is_true(name_article != last_article_link.get_text().lower(), f'Button doesn\'t work')
