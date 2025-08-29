from playwright.sync_api import Page, TimeoutError, expect
from helpers.constants import WebPageUrl, UserCredentials
import allure
from logging import info, debug, warning, error


class StartPage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('#Username')
        self.password_input = page.locator('#Password')
        self.login_button = page.locator('//*[contains(@type, "submit")]')
        self.logout_button = page.get_by_role("link", name="Abmelden")
        self.devices_link = page.get_by_role("link", name="Boxen")
        self.link_to_powerfox_platform = page.get_by_role("link", name="https://www.powerfox.energy")
        self.user_email = page.get_by_role("link", name=UserCredentials.USERNAME)


    @allure.step('And load page')
    def load(self, url) -> None:
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')
        info(f"The webpage {url} has been loaded successfully")

    @allure.step('And login to account')
    def login(self, login, password) -> None:
        self.username_input.fill(login)
        # self.username_input.press('Tab')
        self.password_input.fill(password)
        self.login_button.click()


    @allure.step('And proceed to Devices page')
    def proceed_to_devices_tab(self) -> None:
        self.devices_link.click(timeout=5000)
        self.page.wait_for_url(WebPageUrl.DEVICES_PAGE)


