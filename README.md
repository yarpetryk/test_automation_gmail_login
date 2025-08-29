## Setup (Python 3.10+)

1. Configure a virtual environment for PyCharm: 
   1. File>Settings>Project Interpreter>Settings icon> Add Local 
2. Change Test Runner for PyCharm: 
   1. File>Settings>Tools>Python Integrated Tools>Default test runner>PyTest
3. Execute in terminal: 
   1. pip install -r requirements.txt
4. Change your local settings in config.json'


### Run all tests

```
pytest
```

### Run tests matching given mark expression

```
pytest -m smoke
```


### Run an arbitrary file
```
pytest <NameOfFile>.py
```

### Install playwright browser engine's
```
playwright install
```

### Run playwright test with different options
```
pytest -m <mark> [*options]
options:
--headed
--browser [chromium, firefox, webkit]
--browser-channel [chrome]
--device ["iPhone 13",]
--screenshot [on, off, only-on-failure]
--video [on, off, retain-on-failure]
--tracing [on,]
--output [results,]
--slowmo 2000
--base-url https://portal.powerfox.energy/
```

### Playwright scope
```
page -> function scope (for independent tests)
browser -> session scope (for dependent tests)

```
### Playwright UI interaction
```
input -> fill("John")
input -> type("John) # enter character by character
select -> click()
dropdown -> select_option("1")
radio button -> nth(1).check()
checkbox -> is_checked() -> click()
press key -> press("Enter")
focus on or move to element -> tap()
upload file -> set_input_files("file_location")
wait for start page -> self.page.wait_for_load_state(['networkidle', 'domcontentloaded'])
wait for new page -> wait_for_url("https://...")
wait for dynamic element -> wait_for_selector(), wait_for_element_state("visible"), wait_for_event(event)
wait for static element -> expect(locator).to_be_visible(), expect(locator).to_have_text()
check visibility -> page.is_visible(locator)
handle pop-up -> with page.expect_popup()
scroll -> mouse.wheel(100, 100), scroll_into_view_if_needed()
screenshot -> screenshot(path='')
new browser tab -> def test_login(context) -> page_1 = context.new_page(), page_2 = context.new_page()

```

### Playwright Network Events
```
page.on('request', lambda request: print(request.method, request.url))
page.on("requestfailed", lambda request: print(request.url + " " + request.failure.error_text))
page.on('response', lambda response: print(response.status, response.url))clear
page.on("dialog", lambda dialog: dialog.accept())
page.on ('load', handler)
page.on("domcontentloaded", handler)
page.on("filechooser", lambda file_chooser: file_chooser.set_files("/tmp/myfile.pdf"))
page.on("websocket", handler)

```
### Playwright debug mode
```
PWDEBUG=1 pytest -m smoke

```
### Playwright codegen
```
playwright codegen google.com

```
### Playwright tracing
```
playwright playwright show-trace trace.zip

from playwright.sync_api import sync_Playwright
def run(playwright: Playwright) -> None:
   browser = palywright.chromium.launch(headless=False)
   context = browser.new_context(
      locale='en-EN'
      )
   context.tracing.start(screenshots=True, snapshots=True, sources=True)
   context.tracing.stop(path='trace.zip')
   context.close()
   browser.close()
   
with sync_playwright as playwright:
   run(playwright)

```
### Skip tests
```
@pytest.mark.skip_browser('chromium')
@pytest.mark.only_browser('chromium')
```

### Tests parallel execution
```
pytest-xdist
pytest -n 3
```
### Local storage
```
context.storage_state(path='state.json')
```
### Visual comparison
```
pytest-playwright-visual
assert_snapshot(page.screenshot())

```
### Run an Allure report generation
1. Download and extract Allure into the Program Files (https://github.com/allure-framework/allure2/releases/)
2. Add Path in the system variables to the allure bin folder:
   1. Path (C:\Program Files\allure\bin)


```
pytest --alluredir=allure-results
allure serve ./allure-results
```