"""Module housing  utilities for Login page"""
from logging import info

import allure
from playwright.sync_api import Page, expect


class LoginPage:
    """Class providing utility for Login page"""
    def __init__(self, page: Page) -> None:
        """Constructor method for Login page"""
        self.page = page
        self.sign_in_button = page.get_by_role("link", name="Open the Sign into Gmail page")
        self.email_input = page.locator('//*[contains(@type, "email")]')
        self.password_input = page.locator('//*[contains(@type, "password")]')
        self.login_button = page.locator('//*[contains(@type, "submit")]')
        self.next_button = page.get_by_role("button", name="Next")
        self.inbox_link = page.get_by_role("link",  name="Inbox")
        self.error_message = ''

    @allure.step('And load page')
    def load(self, url: str) -> None:
        """Method for starting the browser with provided url"""
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')
        info(f"The webpage {url} has been loaded successfully")

    @allure.step('And the user logs in to the account')
    def login(self,
              email: str,
              password: str) -> None:
        """Method implements the user logging"""
        self.sign_in_button.click()
        self.email_input.fill(email)
        self.next_button.click()
        self.password_input.fill(password)
        self.next_button.click()

    @allure.step('And the user checks the logging status')
    def is_user_logged_in(self) -> bool:
        """Method implements the user logging validation"""
        expect(self.inbox_link).to_be_visible()
        info("The user has been logged in")
        return True

    @allure.step('And the user provides invalid email')
    def login_with_invalid_username(self,
                                    email: str) -> None:
        """Method implements the user email entering"""
        self.sign_in_button.click()
        self.email_input.fill(email)
        self.next_button.click()

    @allure.step('And the user provides invalid password')
    def login_with_invalid_password(self,
                                    email: str,
                                    password: str) -> None:
        """Method implements the user email and password entering"""
        self.sign_in_button.click()
        self.email_input.fill(email)
        self.next_button.click()
        self.password_input.fill(password)
        self.next_button.click()

    @allure.step('And the user checks the validation warning')
    def is_validation_warning_shown(self,
                                    page: Page,
                                    validation_text: str) -> bool:
        """Method implements the warning validation"""
        page.wait_for_load_state('networkidle')
        el = page.get_by_text(validation_text)
        expect(el).to_be_visible()
        info(f"The validation warning '{validation_text}' is shown")
        return True
