# Sauce Demo test suite

Automated UI tests for [Sauce Demo](https://www.saucedemo.com), a practice e-commerce site, written in Python with pytest and Playwright.

## What's tested

- Logging in as a standard user
- Error handling for a locked-out user
- Error handling for a wrong password
- The products page shows all six products

## Structure

The suite uses the **Page Object Model**: each page of the site has a class in `pages/` that holds its selectors and actions. Tests in `tests/` describe behaviour without touching selectors directly, so a change to the site only needs fixing in one place.

```
pages/      page objects (login, inventory)
tests/      test cases
```

## Running the tests

```bash
pip install -r requirements.txt
playwright install chromium
pytest
```

Watch the browser while tests run:

```bash
pytest --headed --slowmo 500
```
