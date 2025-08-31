### Setup virtual environment
```
1. sudo apt-get install python-pip
2. pip install virtualenv
3. virtualenv venv
4. source venv/bin/activate
```

### Install project dependencies
```
pip install -r requirements.txt
```
### Install playwright browser engines
```
playwright install
```

### Run all tests
```
pytest
```

### Run tests matching given mark expression
```
pytest -m smoke
```

### Run playwright tests with different options
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

### Browse allure reports
```
pytest --alluredir=allure-results
allure serve ./allure-results
```

### Browse testing logs
```
log/results.log
```