import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class ErrorCommentPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://weeklyworldnews.com/wp-comments-post.php'

        super().__init__(web_driver, url)

    error_comment_page_error_text = WebElement(
        xpath="//*[contains(concat(' ', normalize-space(@class), ' '), ' wp-die-message ')]//p")
    error_comment_page_return_page = WebElement(
        xpath="//a")
