
class BookingReport:
    def __inti__self(self , boxex_section_element):
        self.boxex_section_element = boxex_section_element
        self.pull_deal_boxex = self.pull_deal_boxex()
        
    def pull_deal_boxex(self):
        return self.boxex_section_element.find_elements(By.CSS_SELECTOR , 'div[data-testid="property-card"]')