from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
class GoogleTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
           
    def tearDown(self):
      
        # Close the browser
        self.driver.quit()

    def test_search_by_keyword(self):
       
        # Open Google
        self.driver.get("http://www.google.com")

        # Find the search box element and enter a query
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("PBRU")

        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to load (ideally, use WebDriverWait instead of time.sleep)
        time.sleep(5)

        # Print the title of the current page
        print(self.driver.title)

        page_content = self.driver.page_source
        self.assertIn("มหาวิทยาลัยราชภัฏเพชรบุรี", page_content, "Not in Page")



        # def test_search_by_keyword(self): (ถ้าจะเพิ่มตัวเทสที่2ให้เพิ่มkeyword2)


if __name__ == "__main__":
    unittest.main()
