import os

from cffi.backend_ctypes import xrange

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class PressPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://weeklyworldnews.com/press/'

        super().__init__(web_driver, url)

    press_link_further_information = WebElement(
        xpath='(//*[@href="https://drive.google.com/drive/u/2/folders/1kAN-MReULA0gKMZHsl3qoPN6bfWk8OgH"])')

    press_link_main_page = WebElement(
        xpath='(//*[@rel="noopener noreferrer"])[4]')
    press_link_facebook = WebElement(
        xpath='(//*[@class="automize-selected-node automize-selected-transition"])')
    press_link_instagram = WebElement(
        xpath='(//*[@href="https://www.instagram.com/weeklyworldnewsofficial/"])')
    press_link_twitter = WebElement(
        xpath='(//*[@href="http://twitter.com/weeklyworldnews"])')
    press_link_youtube = WebElement(
        xpath='(//*[@rel="noopener noreferrer"])[8]')
    press_link_linkedin = WebElement(
        xpath='(//*[@href="https://www.linkedin.com/company/weekly-world-news"])')
