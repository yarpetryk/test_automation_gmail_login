"""Module housing tests for Login flow"""
import pytest
from playwright.sync_api import Page

from helpers.configs import UserCredentials, WebPageUrl
from pages.login_page import LoginPage


class TestLogin:
    """Test class for login flow"""
    @pytest.mark.smoke
    def test_login_happy_path(self,
                              login_page: LoginPage) -> None:
        """Tests login flow with a happy path"""
        login_page.load(WebPageUrl.HOME_PAGE)
        login_page.login(
            email=UserCredentials.EMAIL,
            password=UserCredentials.PASSWORD)
        assert login_page.is_user_logged_in()

    @pytest.mark.regression
    @pytest.mark.parametrize(
        'email, validation_text',
        [
            ('', 'Enter an email or phone number'),
            (UserCredentials.EMAIL_INVALID, 'This browser or app may not be secure'),
            (UserCredentials.EMAIL_WRONG_DOMAIN, 'This browser or app may not be secure')
        ])
    def test_login_email_is_incorrect(self,
                                      page: Page,
                                      login_page: LoginPage,
                                      email: str,
                                      validation_text: str) -> None:
        """Test login flow with an incorrect email:
            - login flow with empty email input
            - login flow with wrong email
            - login flow with wrong email domain"""
        login_page.load(WebPageUrl.HOME_PAGE)
        login_page.login_with_invalid_username(email=email)
        assert login_page.is_validation_warning_shown(page,
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
                                   login_page: LoginPage,
                                   password: str,
                                   validation_text: str) -> None:
        """Test login flow with an incorrect password:
            - login flow with empty password
            - login flow with wrong password"""
        login_page.load(WebPageUrl.HOME_PAGE)
        login_page.login_with_invalid_password(
            email=UserCredentials.EMAIL,
            password=password
        )
        assert login_page.is_validation_warning_shown(page,
                                                      validation_text=validation_text)