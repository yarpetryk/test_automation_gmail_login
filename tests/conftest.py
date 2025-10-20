"""
Module housing fixtures for all tests
"""
"""
Module housing fixtures for all tests
"""
import pytest
from playwright.sync_api import Page
from playwright.sync_api import Page

from pages.login_page import LoginPage

from pytest_testrail.plugin import PyTestRailPlugin
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture for Login page"""
    return LoginPage(page)

def pytest_configure(config):
    original_add_result = PyTestRailPlugin.add_result
    def patched_add_result(self, *args, **kwargs):
        if 'test_parametrize' in kwargs:
            kwargs['test_parametrize'] = ''
        return original_add_result(self, *args, **kwargs)
    PyTestRailPlugin.add_result = patched_add_result
