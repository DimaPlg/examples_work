import time

import allure
import pytest_check as check
from pytest_check import equal
from selenium import webdriver

from locators.locators_article_page import ArticlePage
from locators.locators_error_invalid_input_date_comment import ErrorCommentPage
from page.elements import WebElement

@allure.story('Тест для проверки страницы статьи')
@allure.feature('Тест для проверки кнопки возврата на главную страницу сайта')
def test_home_return_btn(web_browser):
    page = ArticlePage(web_browser)
    btn_home = page.article_page_home_link
    WebElement.scroll_to_element(btn_home)
    btn_home.click()
    time.sleep(2)

    check.equal(page.get_current_url(), 'https://weeklyworldnews.com/',
                f'Current url{page.get_current_url()}')

@allure.story('Тест для проверки страницы статьи')
@allure.feature('Тест на соответствие названия статьи')
def test_article_page_name(web_browser):
    article_name_expected = 'BABY BUNNIES TURN INTO FLESH-HUNGRY ZOMBIE RABBITS'
    page = ArticlePage(web_browser)
    article_name = page.article_page_name_article
    WebElement.scroll_to_element(article_name)
    time.sleep(2)
    check.equal(article_name.get_text().upper(), article_name_expected,
                f'name article{article_name.get_text().upper()}, but needed {article_name_expected}')

@allure.story('Тест для проверки страницы статьи')
@allure.feature('Тест для проверки кнопок для пересылки статьи')
def test_article_page_links_send_btn(web_browser):
    page = ArticlePage(web_browser)

    TEST_BTN = [
        page.article_page_reddit_link_share,
        page.article_page_more_link_share,
        page. article_page_facebook_link_share,
        page. article_page_twitter_link_share,
    ]

    for button in TEST_BTN:
        WebElement.scroll_to_element(button)
        time.sleep(5)
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(button.is_visible(), f'unvisible')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(button.is_clickable(), f'uncklik')



@allure.story('Тест для проверки страницы статьи')
@allure.feature('Тест для проверки блока с ссылками на статьи со схожей тематикой')
def test_article_page_links_article_with_similar_subject(web_browser):
    main_teme_article = ['bunny', 'rabbit']
    page = ArticlePage(web_browser)

    SIMILAR_ARTICLE = [
        page. article_page_related_first_link,
        page. article_page_related_second_link,
        page. article_page_related_third_link
    ]
    for element in SIMILAR_ARTICLE:
        WebElement.scroll_to_element(element)
        time.sleep(2)
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(element.is_visible(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(element.is_clickable(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на тематику'):
            check.is_true(main_teme_article[0] in element.get_text().lower() or
                          main_teme_article[1] in element.get_text().lower(),
                          f'No such teme')

@allure.story('Тест для проверки страницы статьи')
@allure.feature('Тест для проверки окна ввода комментариев')
def test_article_page_send_comment_massage(web_browser):
    page = ArticlePage(web_browser)

    TEST_COMMENT_VALUE = [
        # ['bunny', 'Kirill', 'veubavaubreussa-1618@yopmail.com', 'bunny'],
        ['', 'Kirill', 'pleshko.dima19@gmail.com', 'please type your send_comment text'],
        ['bunny', '', 'veubavaubreussa-1618@yopmail.com', 'please fill the required fields'],
        ['bunny', 'Kirill', '', 'please fill the required fields'],
        ['https://weeklyworldnews.com/topstory/45176/man-evolved-from-rabbits/', 'Kirill',
         'veubavaubreussa-1618@yopmail.com', 'please type your send_comment text'],
        # ['bunny', 'K', 'veubavaubreussa-1618@yopmail.com', 'bunny'],
        ['bunny', 'Kirill', 'l.com', 'please enter a valid email address'],
        ['bunny', 'Kirill', 'm', 'please enter a valid email address'],
    ]

    comment_box = page. article_page_comment_input_box
    name_box = page. article_page_name_author_comment
    email_box = page. article_page_email_author_comment
    btn_send_comment = page. article_page_btm_post_comment
    send_comment = page. article_page_comment_text_massage
    current_url = page.get_current_url()

    for comment, name, email, result in TEST_COMMENT_VALUE:
        WebElement.scroll_to_element(comment_box)
        time.sleep(2)
        comment_box.send_keys(comment)
        WebElement.scroll_to_element(name_box)
        time.sleep(2)
        name_box.click()
        name_box.send_keys(name)
        WebElement.scroll_to_element(email_box)
        time.sleep(2)
        email_box.click()
        email_box.send_keys(email)
        time.sleep(5)

        WebElement.scroll_to_element(btn_send_comment)
        time.sleep(2)
        btn_send_comment.click()
        if page.get_current_url() == current_url:
            WebElement.scroll_to_element(send_comment)
            time.sleep(2)
            check.is_true(result in send_comment.get_text().lower(), f'Unexpected response:{comment.get_text().lower()}')
        else:
            page_error = ErrorCommentPage(web_browser)
            error_answer = page_error.error_comment_page_error_text
            WebElement.scroll_to_element(error_answer)
            check.is_true(result in error_answer.get_text().lower(), f'Unexpected response:{comment.get_text().lower()}')




@allure.story('Тест для проверки страницы статьи')
@allure.feature('Тест для проверки блока с ссылками на статьи на боковой панели')
def test_article_page_side_bar_links_article(web_browser):
    page = ArticlePage(web_browser)

    SIDE_BAR_LINKS_ARTICLE = [
        page. article_page_side_bar_links_first,
        page. article_page_side_bar_links_last,
    ]
    for element in SIDE_BAR_LINKS_ARTICLE:
        WebElement.scroll_to_element(element)
        time.sleep(2)
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(element.is_visible(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(element.is_clickable(), f'{element.get_text()}')