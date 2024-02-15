import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchByKeyword1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://localhost/Customer/Customer.html")

    def test_search_by_keyword1(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canonc")
        ageInput.send_keys("2")
        
        submitButton.click()

        # Waiting for the result to appear
        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohn", result)

        # Capture a screenshot
        self.driver.save_screenshot("screenshot.png")

    def tearDown(self):
        time.sleep(2)  # Adding some delay before closing the browser
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
