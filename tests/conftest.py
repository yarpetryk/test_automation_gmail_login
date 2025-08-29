import pytest
from logging import info


from playwright.sync_api import Playwright, Page, expect, APIRequestContext, Route
from helpers.constants import UserCredentials, WebPageUrl
from pages.start_page import StartPage
from pages.devices_page import DevicesPage


@pytest.fixture
def start_page(page: Page) -> StartPage:
    return StartPage(page)

@pytest.fixture
def devices_page(page: Page) -> DevicesPage:
    return DevicesPage(page)

@pytest.fixture
# def login_set_up(page: Page, url: str) -> None:
def login_set_up(page: Page) -> Page:
    username_input = page.locator('#Username')
    password_input = page.locator('#Password')
    login_button = page.locator('//*[contains(@type, "submit")]')
    logout_button = page.get_by_role("link", name="Abmelden")
    page.goto(WebPageUrl.START_PAGE)
    page.wait_for_load_state('networkidle')
    info(f"The webpage {WebPageUrl.START_PAGE} has been loaded successfully")
    username_input.fill(UserCredentials.USERNAME)
    password_input.fill(UserCredentials.PASSWORD)
    login_button.click()
    expect(logout_button).to_be_visible()
    info("User logged in successfully")
    yield page
    page.close()

@pytest.fixture
def api_request_context(playwright: Playwright) -> APIRequestContext:
    request_context = playwright.request.new_context(
        base_url="https://backend.powerfox.energy",
        http_credentials={
            'username': 'lsqateam@gmail.com',
            'password': 'Abc123!!'
        })
    return request_context

@pytest.fixture
def mock_server_response(page: Page):
    data = {

    }
    page.on('request', lambda request: print(request.method, request.url))
    page.on('response', lambda response: print(response.status, response.url))
    page.route("https://portal.powerfox.energy/Admin/Devices", lambda status_code: status_code.fulfill(status=401))
    page.route("https://portal.powerfox.energy/Admin/Devices", lambda response: response.fulfill(json=data))
    page.route("https://portal.powerfox.energy/Admin/Devices", lambda response: response.fulfill(path="mock_data.html"))
    yield page
