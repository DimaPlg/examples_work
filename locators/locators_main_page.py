import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://weeklyworldnews.com/'

        super().__init__(web_driver, url)

    header_wwn = WebElement(xpath="//*[@rel='home']")
    btn_header_logo = WebElement(xpath='//*[@alt="Weekly World News"]')
    headers_gif = WebElement(xpath='//*[@class="wp-image-185815"]')
    main_page_title = WebElement(xpath='//h1')
    main_menu_headliners = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/category/headlines/']")
    main_menu_free_subscription = WebElement(
        xpath='(//*[@aria-label="Primary"]//a)[3]')
    main_menu_shop = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.hellomerch.com/']")
    main_menu_aliens = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/category/aliens/']")
    main_menu_gootans = WebElement(
        xpath='(//*[@aria-label="Primary"]//a)[6]')
    main_menu_zeebans = WebElement(
        xpath='(//*[@aria-label="Primary"]//a)[7]')
    main_menu_ufo_sightings = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/tag/ufo-sightings/']")
    main_menu_mutants = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/category/mutants/']")
    main_menu_mutants_zombies = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/tag/zombies/']")
    main_menu_mutants_bigfoot = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/tag/bigfoot/']")
    main_menu_mutants_phd_ape = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/tag/phd-ape/']")
    main_menu_mutants_bat_boy = WebElement(
        xpath="//nav[@id='site-navigation']//ul[@class='sub-menu']//a[@href='https://weeklyworldnews.com/tag/bat-boy/']")
    main_menu_mutants_vampires = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/tag/vampires/']")
    main_menu_mutants_manigator = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/tag/manigator/']")
    main_menu_bat_boy = WebElement(xpath='(//*[@aria-label="Primary"]//a)[16]')

    main_menu_greatest_people = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/worlds-greatest-people-2021/']")
    main_menu_press = WebElement(xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/press/']")
    main_menu_about = WebElement(xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/about/']")
    main_menu_contact = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://weeklyworldnews.com/contact/']")
    main_menu_search_bar = WebElement(
        xpath="(//*[@aria-label='Open Search Bar'])[4]")
    main_menu_input_search_bar = WebElement(
        xpath='(//*[@name="s"])[2]')
    main_menu_youtube_chanel = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://www.youtube.com/channel/UCAcs6RIm6jYYsTwNA0ljMNQ']")
    main_menu_facebook = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://www.facebook.com/weeklyworldnews/']")
    main_menu_instagram = WebElement(
        xpath="//nav[@id='site-navigation']//a[@href='https://www.instagram.com/weeklyworldnewsofficial']")
    main_menu_twitter = WebElement(xpath="//nav[@id='site-navigation']//a[@href='https://twitter.com/weeklyworldnews']")

    main_page_article_link_first = WebElement(
        xpath='(//*[@rel="bookmark"])[last()-8]')
    main_page_article_link_first_author = WebElement(
        xpath='(//*[@itemprop="name"])[last()-8]')
    main_page_article_link_last = WebElement(
        xpath='(//*[@rel="bookmark"])[last()-0]')
    main_page_article_link_last_author = WebElement(
        xpath='(//*[@itemprop="name"])[last()-0]')

    main_page_btm_for_more_news = WebElement(
        xpath="//*[contains(concat(' ', normalize-space(@class), ' '), ' button ')]")


