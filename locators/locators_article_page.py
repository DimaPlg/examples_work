import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class ArticlePage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://weeklyworldnews.com/mutants/186349/baby-bunnies-turn-into-flesh-hungry-zombie-rabbits/'

        super().__init__(web_driver, url)

    article_page_home_link = WebElement(
        xpath='(//article//a)[1]')
    article_page_author_articles = WebElement(
        xpath='//*[@itemprop="name"]')
    article_page_name_article = WebElement(
        xpath='//h1')
    article_page_facebook_link_share = WebElement(
        xpath='//*[@data-href="https://weeklyworldnews.com/mutants/186349/baby-bunnies-turn-into-flesh-hungry-zombie-rabbits/"]')
    article_page_twitter_link_share = WebElement(
        xpath='//*[@title="X Post Button"]')
    article_page_reddit_link_share = WebElement(
        xpath='(//*[@rel="nofollow noopener noreferrer"])[1]')
    article_page_more_link_share = WebElement(
        xpath='(//article//a)[4]')
    article_page_more_link_share_save = WebElement(
        xpath='//*[@data-pin-log="button_pinit"]')
    article_page_more_link_share_email = WebElement(
        xpath='(//*[@rel="nofollow noopener noreferrer"])[last()-0]')
    article_page_related_first_link = WebElement(
        xpath='(//article//h4)[1]')
    article_page_related_second_link = WebElement(
        xpath='(//article//h4)[2]')
    article_page_related_third_link = WebElement(
        xpath='(//article//h4)[3]')
    article_page_ref_to_current_link = WebElement(
        xpath='//*[@rel="prev"]')
    article_page_comment_text_massage = WebElement(
        xpath= '(//*[@itemprop="text"])[last()-0]')
    article_page_comment_input_box = WebElement(
        xpath='//*[@name="comment"]')
    article_page_name_author_comment = WebElement(
        xpath='//*[@id="respond"]//*[@name="author"]')
    article_page_email_author_comment = WebElement(
        xpath='//*[@name="email"]')
    article_page_url_author_comment = WebElement(
        xpath='//*[@name="url"]')
    article_page_btm_post_comment = WebElement(
        xpath='//*[@name="submit"]')
    article_page_learn_data_processed = WebElement(
        xpath='//*[@rel="nofollow noopener"]')

    article_page_shop_link = WebElement(
        xpath='(//*[@decoding="async"])[4]')

    article_page_side_bar_links_first = WebElement(
        xpath='(//*[@id="right-sidebar"]//li)[1]')
    article_page_side_bar_links_last = WebElement(
        xpath='(//*[@id="right-sidebar"]//li)[last()-0]')
