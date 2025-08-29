"""
Module housing fixtures for all tests
"""
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture for Login page"""
    return LoginPage(page)
