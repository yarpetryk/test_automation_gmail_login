"""
Module housing fixtures for all tests
"""
import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage


@pytest.fixture
def home_page(page: Page) -> HomePage:
    """Fixture for Home page"""
    return HomePage(page)
