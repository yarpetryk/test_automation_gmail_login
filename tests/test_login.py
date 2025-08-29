"""Module housing tests for Login flow"""
import pytest
from playwright.sync_api import Page

from helpers.configs import UserCredentials, WebPageUrl
from pages.home_page import HomePage


class TestLogin:
    """Test class for login flow"""
    @pytest.mark.smoke
    def test_login_happy_path(self,
                              home_page: HomePage) -> None:
        """Tests login flow with a happy path"""
        home_page.load(WebPageUrl.HOME_PAGE)
        home_page.login(
            email=UserCredentials.EMAIL,
            password=UserCredentials.PASSWORD)
        assert home_page.is_user_logged_in()

    @pytest.mark.regression
    @pytest.mark.parametrize(
        'email, validation_text',
        [
            ('', 'Enter an email or phone number'),
            (UserCredentials.EMAIL_INVALID, 'Couldn’t find your Google Account'),
            (UserCredentials.EMAIL_WRONG_DOMAIN, 'Enter a valid email or phone number')
        ])
    def test_login_email_is_incorrect(self,
                                      page: Page,
                                      home_page: HomePage,
                                      email: str,
                                      validation_text: str) -> None:
        """Test login flow with an incorrect email:
            - login flow with empty email input
            - login flow with wrong email
            - login flow with wrong email domain"""
        home_page.load(WebPageUrl.HOME_PAGE)
        home_page.login_with_invalid_username(email=email)
        assert home_page.is_validation_warning_shown(page,
                                                     validation_text=validation_text)

    @pytest.mark.regression
    @pytest.mark.parametrize(
        'password, validation_text',
        [
            ('', 'Enter a password'),
            (UserCredentials.PASSWORD_INVALID, 'Wrong password')
         ])
    def test_password_is_incorrect(self,
                                   page: Page,
                                   home_page: HomePage,
                                   password: str,
                                   validation_text: str) -> None:
        """Test login flow with an incorrect password:
            - login flow with empty password
            - login flow with wrong password"""
        home_page.load(WebPageUrl.HOME_PAGE)
        home_page.login_with_invalid_password(
            email=UserCredentials.EMAIL,
            password=password
        )
        assert home_page.is_validation_warning_shown(page,
                                                     validation_text=validation_text)