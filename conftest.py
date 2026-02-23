"""
Configuration pytest partagée : fixture du driver Chrome (headless pour CI).
"""

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    _driver = webdriver.Chrome(options=options)
    yield _driver
    _driver.quit()
