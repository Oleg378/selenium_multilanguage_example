import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_open_book_page(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(5)
    time.sleep(10)
    try:
        browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    except NoSuchElementException:
        assert False, '<.btn-add-to-basket> element has not found!'



# pytest --language=es
# or:
# pytest --language=fr --browser_name=firefox test_items.py

