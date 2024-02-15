import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGoogleWebsite(unittest.TestCase):

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

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohn", result)

        time.sleep(2)

    def test_search_by_keyword2(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("Johnj")
        lastNameInput.send_keys("canoncanoncano")
        ageInput.send_keys("149")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: Johnj", result)

        time.sleep(2)

    def test_search_by_keyword3(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjo")
        lastNameInput.send_keys("canoncanoncanon")
        ageInput.send_keys("150")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjo", result)

        time.sleep(2)

    def test_search_by_keyword4(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("Johnjohnjohnjo")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: Johnjohnjohnjo", result)

        time.sleep(2)

    def test_search_by_keyword5(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjohnjohnjoh")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohnjohnjoh", result)

        time.sleep(2)

    def test_search_by_keyword6(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("John")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: John", result)

        time.sleep(2)

    def test_search_by_keyword7(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjohnjohnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohnjohnjohn", result)

        time.sleep(2)

    def test_search_by_keyword8(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("cano")
        ageInput.send_keys("75")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohn", result)

        time.sleep(2)

    def test_search_by_keyword9(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncanoncanonc")
        ageInput.send_keys("75")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohn", result)

        time.sleep(2)

    def test_search_by_keyword10(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("0")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohn", result)

        time.sleep(2)

    def test_search_by_keyword11(self):
        firstNameInput = self.driver.find_element(By.ID, "firstName")
        lastNameInput = self.driver.find_element(By.ID, "lastName")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("151")
        
        submitButton.click()

        result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname"))).text
        self.assertEqual("First Name: johnjohn", result)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
