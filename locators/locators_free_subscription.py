import os

from page.base_page import WebPage
from page.elements import WebElement


class SubscriptionPage(WebPage):

    def __init__(self, web_driver, url='https://weeklyworldnews.com/weekly-world-newsletter/'):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://weeklyworldnews.com/weekly-world-newsletter/'

        super().__init__(web_driver, url)

    free_subscription_email_box = WebElement(
        xpath='(//*[@aria-required="true"])[1]')
    free_subscription_first_name_box = WebElement(xpath='(//*[@id="mce-FNAME"])')
    free_subscription_last_name = WebElement(xpath='(//*[@id="mce-LNAME"])')
    free_subscription_email_format_html = WebElement(xapth='(//*[@class="mc-field-group input-group"])//li[1]')
    free_subscription_email_format_text = WebElement(xapth='(//*[@class="mc-field-group input-group"])//li[2]')
    free_subscription_subscribe = WebElement(xpath='//*[@name="subscribe"]')

    free_subscription_made_with_mailchimp = WebElement(xpath='(//*[@href="http://eepurl.com/hO_KD9"])')
    free_subscription_view_previous_campaigns = WebElement(xpath='(//*[@title="View previous campaigns"])')