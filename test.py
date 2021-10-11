from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
import pytest
import time


class TestCICD:
    def test_cicd(self):
        try:
            # Chromeを操作
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            url = "http://127.0.0.1:5000/demo"
            driver.get(url)
            time.sleep(5)
            txt = driver.find_element_by_xpath('/html/body').text
            assert txt == 'demo'
        except Exception as e:
            assert False, e
        finally:
            driver.quit()