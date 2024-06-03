from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__(service=ChromeService(ChromeDriverManager().install()))
        self.implicitly_wait(10)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        try:
            wait = WebDriverWait(self, 10)
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
            element.click()
        except:
            pass
    
    def change_currencry(self , currency=None):
        # print(currency);
        currencyElement = self.find_element(By.CSS_SELECTOR , "button[aria-label='Prices in Indian Rupee']")
        currencyElement.click()
        self.find_element(By.XPATH , f"//div[normalize-space()='{currency}']").click()   
        try:
            wait = WebDriverWait(self, 5)
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
            element.click()
        except:
            pass

    def select_place_to_go(self , place=None):
        input_box = self.find_element(By.XPATH , "//input[@id=':re:']")
        input_box.send_keys(place)
        time.sleep(2)
        self.find_element(By.XPATH , "//li[@id='autocomplete-result-0']").click()
        time.sleep(2)