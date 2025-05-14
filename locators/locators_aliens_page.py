import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class AliensPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://weeklyworldnews.com/category/aliens/'

        super().__init__(web_driver, url)

        aliens_page_article_link_category_first = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-8]/*[1]')
        aliens_page_article_link_category_second = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-7]/*[1]')
        aliens_page_article_link_category_third = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-6]/*[1]')
        aliens_page_article_link_category_four = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-5]/*[1]')
        aliens_page_article_link_category_fifth = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-8]/*[1]')
        aliens_page_article_link_category_six = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-8]/*[1]')
        aliens_page_article_link_category_seven = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-8]/*[1]')
        aliens_page_article_link_category_eight = WebElement(
            xpath='(//*[@aria-label="Entry meta"])[last()-8]/*[1]')

        aliens_page_btn_add_more = WebElement(xpath='//*[@class="masonry-load-more load-more  "]')