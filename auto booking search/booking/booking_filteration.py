from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const

class BookingFilteration(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(BookingFilteration, self).__init__(service=ChromeService(ChromeDriverManager().install()))
        self.implicitly_wait(10)
        self.maximize_window()
        
    def apply_star_rating(self):
        try:
            wait = WebDriverWait(self, 5)
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
            print()
            element.click()
        except:
            pass
        star_element = self.find_element(By.CSS_SELECTOR , f"body > div:nth-child(6) > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(22) > div:nth-child(7)")
        star_element.click()
        print(star_element)
        time.sleep(6)