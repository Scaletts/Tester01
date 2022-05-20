import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1348028")
        self.assertIn('Log in to Facebook', driver.title)
        username = driver.find_element(By.XPATH, "//*[@id=\"email\"]")
        username.send_keys("duongtruongtho12@gmail.com")
        password = driver.find_element(By.XPATH, "//*[@id=\"pass\"]")
        password.send_keys("05217416aa")
        btn = driver.find_element(By.XPATH, "//*[@id=\"loginbutton\"]")
        btn.click()
        mtn = driver.find_element(By.XPATH, "//*[@id=\"loginform\"]/div[2]/div[2]")
        mtn.click()
        stn = driver.find_element(By.XPATH, "//*[@id=\"login_link\"]/div/a")
        stn.click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
