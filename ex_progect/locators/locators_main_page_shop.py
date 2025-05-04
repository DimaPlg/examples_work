import os

from cffi.backend_ctypes import xrange

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://weeklyworldnews.myshopify.com/'

        super().__init__(web_driver, url)

    wwn_shop_page_header_logo = WebElement(xpath='(//*[@data-sizes="auto"])[1]]')

    wwn_shop_page_menu_newsroom = WebElement(xpath='(//*[@aria-current="page"])[1]')
    wwn_shop_page_menu_publication = WebElement(xpath='(//*[@data-section-id="header"]//span)[2]')
    wwn_shop_page_menu_apparel = WebElement(xpath='(//*[@data-section-id="header"]//span)[3]')
    wwn_shop_page_menu_this_not_that = WebElement(xpath='(//*[@data-section-id="header"]//span)[4]')
    wwn_shop_page_menu_wwn_fine_art = WebElement(xpath='(//*[@data-section-id="header"]//span)[5]')
    wwn_shop_page_menu_all_our_stuff = WebElement(xpath='(//*[@data-section-id="header"]//span)[6]')
    wwn_shop_page_menu_search_bar = WebElement(xpath='//*[@aria-controls="dialog"]')
    wwn_shop_page_menu_search_bar_btn_close = WebElement(xpath='((//*[@aria-label="Search"])[1]//button)[3]')
    wwn_shop_page_menu_cart = WebElement(xpath='(//*[@data-section-id="header"]//a)[8]')

    wwn_shop_page_get_creates_covers_btn = WebElement(
        xpath='//*[@aria-label="Get Greatest Covers!: Weekly World News Greatest Covers Limited Print Edition"]')
    wwn_shop_page_btn_buy_tshirt = WebElement(
        xpath='//*[@aria-label="Buy T-shirt: The Zombie Wedding T-Shirt"]')

    wwn_shop_page_box_enter_subscribe_email = WebElement(xpath='//*[@aria-label="Email address"]')
    wwn_shop_page_btn_subscribe_email = WebElement(xpath='//*[@name="commit"]')

    wwn_shop_page_link_search_page = WebElement(xpath='(//*[@data-section-id="footer"]//li)[1]')
    wwn_shop_page_link_personal_information_policy = WebElement(xpath='(//*[@data-section-id="footer"]//li)[2]')

    wwn_shop_page_change_currency_change = WebElement(xpath='//*[@aria-controls="currency-list"]')
    wwn_shop_page_change_currency_change_afn = WebElement(xpath='//*[@data-value="AFN"]')
    wwn_shop_page_change_currency_change_etb = WebElement(xpath='//*[@data-value="ETB"]')
    wwn_shop_page_change_currency_change_nzd = WebElement(xpath='//*[@data-value="NZD"]')
    wwn_shop_page_change_currency_change_usd = WebElement(xpath='//*[@data-value="USD"]')
    wwn_shop_page_change_currency_change_yer = WebElement(xpath='//*[@data-value="YER"]')

    wwn_shop_page_facebook = WebElement(xpath='(//*[@data-section-id="footer"]//*[@aria-hidden="true"])[1]')
    wwn_shop_page_x = WebElement(xpath='(//*[@data-section-id="footer"]//*[@aria-hidden="true"])[2]')
    wwn_shop_page_instagram = WebElement(
        xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' social-icons__link ')])[3]")
    wwn_shop_page_youtube = WebElement(
        xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), ' social-icons__link ')])[4]")

    wwn_shop_page_btn_return_main_page = WebElement(xpath='(//*[@title=""])[1]')
    wwn_shop_page_btn_shopify_shop_page = WebElement(xpath='(//*[@target="_blank"])[1]')

