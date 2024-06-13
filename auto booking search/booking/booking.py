from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__(service=ChromeService(ChromeDriverManager().install()))
        self.implicitly_wait(2)
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
        input_box = self.find_element(By.XPATH , "(//input[@id=':r7:'])[1]")
        input_box.send_keys(place)
        time.sleep(2)
        self.find_element(By.XPATH , "//li[@id='autocomplete-result-0']").click()
        
    def select_dates(self , checkin_date=None , checkout_date=None):
        try:
            checkin_element = self.find_element(By.CSS_SELECTOR, f"span[data-date='{checkin_date}']")
            checkin_element.click()
            
            checkout_element = self.find_element(By.CSS_SELECTOR, f"span[data-date='{checkout_date}']")
            checkout_element.click()
            time.sleep(2)
        except:
            pass            
    
    def select_adults(self, count=2):
        dropdown = self.find_element(By.CSS_SELECTOR , "span[data-testid='searchbox-form-button-icon']")
        dropdown.click()
        
        while True:
            try:
                decrease_adults = self.find_element(By.XPATH , '/html[1]/body[1]/div[3]/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]')
                decrease_adults.click()
                valueElement = self.find_element(By.CSS_SELECTOR , 'body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(2)')
                val = valueElement.get_attribute('innerHTML')
                if(val == '1'):
                    break
            except: 
                pass
        while True:
            valueElement = self.find_element(By.CSS_SELECTOR , 'body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(2)')
            val = valueElement.get_attribute('innerHTML')
            if(val == count):
                break
            increase_adults = self.find_element(By.CSS_SELECTOR , 'body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)')
            increase_adults.click()
        time.sleep(2)
        
    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR  , "button[type='submit']")
        search_button.click()
        time.sleep(1)
        try:
            wait = WebDriverWait(self, 5)
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
            element.click()
        except:
            pass
    
    def apply_star_rating(self , star=0):
        try:
            wait = WebDriverWait(self, 5)
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
            element.click()
        except:
            pass
        try:
            star_element = self.find_element(By.CSS_SELECTOR , f'div[data-filters-item="class:class={star}"]')            
            star_element.click()
            time.sleep(2)
        except:
            print("no hotels found for this star rating")
    
    def sort_lowest_to_highest(self):
        button = self.find_element(By.CSS_SELECTOR , 'button[data-testid="sorters-dropdown-trigger"]')
        button.click()
        self.find_element(By.CSS_SELECTOR , 'button[data-id="class_asc"]').click()
    
    def report_results(self):
        values = []
        hotel_title_object = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="title"]')
        hotel_price_object = self.find_elements(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]')
        # print(len(hotel_price))
        
        # for i in range(10):
        # print(hotel_score);
        table = PrettyTable(
            field_names=["Hotel Name" , "Hotel Price" , "Hotle Score"]
        ) 
        for i in range(len(hotel_title_object)):
            hotel_title = hotel_title_object[i].get_attribute('innerText') 
            hotel_price = hotel_price_object[i].get_attribute('innerText')
            
            hotel_score_object = self.find_elements(By.XPATH, f"(//div[@class='f13857cc8c e008572b71'])[{i+1}]")
            # print(hotel_score_object)
            hotel_score = (hotel_score_object[0].get_attribute('innerText')[:3])
            temp = ([hotel_title , 
                           hotel_price , 
                           hotel_score])
            table.add_row(temp)
        print(table)
        
        