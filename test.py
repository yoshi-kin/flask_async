from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
import pytest


class TestCICD:
    def test_cicd(self):
        # Chromeを操作
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        url = "http://127.0.0.1:5000/demo"
        driver.get(url)
        txt = driver.find_element_by_xpath('/html/body').text
        assert txt == 'demo'
