import time

import allure
import pytest_check as check

from locators.locators_free_subscription import SubscriptionPage
from page.elements import WebElement

@allure.story('Тест для проверки подписку на бесплатную рассылку')
@allure.feature('Тест для проверки полей ввода информации для подписки на рассылку')
def test_free_subscription_offer_view(web_browser):
    page = SubscriptionPage(web_browser)

    TEST_INPUT_SUBSCRIBE_PERSON_INFO=[
        ('example234+d5gq2kha2y@gmail.com', 'Dima','Plushkin', True, True),
        ('', 'Dima', 'Plushkin', True, False),
        ('example234+d5gq2kha2y@gmail.com', '', 'Plushkin', False, False),
        ('example234+d5gq2kha2y@gmail.com', 'Dima', '', True, True),
        ('s,21', 'Dima', 'Plushkin', False, False),
        ('example234+d5gq2kha2y@gmail.com', '   ', 'Plushkin', False, False),
        ('example234+d5gq2kha2y@gmail.com', '3113', 'Plushkin', True, True),
    ]

    for email, first_name, last_name, selected_format, result in TEST_INPUT_SUBSCRIBE_PERSON_INFO:

        # WebElement.scroll_to_element(page.free_subscription_email_box)
        page.scroll_down(200)
        time.sleep(1)
        page.free_subscription_email_box.click()
        page.free_subscription_email_box.send_keys(email)

        time.sleep(1)
        page.free_subscription_first_name_box.send_keys(first_name)
        time.sleep(1)
        page.free_subscription_last_name.send_keys(last_name)
        time.sleep(1)
        if selected_format:
            page.free_subscription_email_format_html.click()
        else:
            page.free_subscription_email_format_text.click()
        time.sleep(1)
        cur_url = page.get_current_url()
        page.free_subscription_subscribe.click()
        time.sleep(2)

        check.equal(page.get_current_url() != cur_url,result,f'Current url{page.get_current_url()}')

@allure.story('Тест для проверки подписку на бесплатную рассылку')
@allure.feature('Тест для проверки блока с ссылками на дополнительные ресурсы')
def test_free_subscription_info_links(web_browser):
    page = SubscriptionPage(web_browser)

    FREE_SUB_INFO_LINKS = [
        page. free_subscription_made_with_mailchimp,
        page. free_subscription_view_previous_campaigns,
    ]
    for element in FREE_SUB_INFO_LINKS:
        WebElement.scroll_to_element(element)
        time.sleep(2)
        with allure.step(f'Проверка элемента на отображение'):
            check.is_true(element.is_visible(), f'{element.get_text()}')
        with allure.step(f'Проверка элемента на кликабельность'):
            check.is_true(element.is_clickable(), f'{element.get_text()}')