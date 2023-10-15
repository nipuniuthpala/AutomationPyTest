import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from config import(
    get_chrome_web_driver,
    get_web_driver_options,
    set_ignore_certificate_error,
    base_url,
    depart,
    arrive,
    departure_date,
    secure,
    
)

class MyTrip:
    def __init__(self,base_url):
        
        options = get_web_driver_options()
        
        self.base_url = base_url
        self.driver = get_chrome_web_driver(options)
        set_ignore_certificate_error(options)
        
        self.act = ActionChains(self.driver)
        
        
    
    def run_script(self):
        
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.to_from_date()
        self.get_date()
        self.choose_flight()
        self.review()
        time.sleep(2)
        self.driver.quit()
    
    def to_from_date(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='toCity']").send_keys(arrive)
    
        time.sleep(2)
        self.act.send_keys(Keys.DOWN,Keys.ENTER).perform()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@id='fromCity']").send_keys(depart)
        time.sleep(2)
        
        self.act.send_keys(Keys.DOWN,Keys.ENTER).perform()
        time.sleep(2)
    
    def get_date(self):

    #    time.sleep(2)
    #    element = self.driver.find_element_by_xpath("//p[@data-cy='departureDate']")
    #    #element = self.driver.find_element_by_id("departure")

    #    time.sleep(2)
    #    element.click()

    #    check = self.driver.find_element_by_xpath("//div[@aria-label='" +departure_date+ "']")
    #    check.click()
        #if check.get_attribute('aria-disabled') == 'false':
        #    check.click()
        #else:
        #    print("Flight not available on that day") 

        time.sleep(2)
        self.driver.find_element_by_class_name('widgetSearchBtn').click()

        time.sleep(3)                 

    def choose_flight(self):
        
        element = self.driver.find_element_by_xpath("//button[@class='ViewFareBtn  text-uppercase ']")
        element1 = self.driver.find_element_by_xpath("//button[@class='button corp-btn latoBlack buttonPrimary fontSize13  ']")
        element2 = self.driver.find_elements_by_class_name('fli_primary_btn')
        print(element,element1)
        element.click()
        element1.click()
        
    def review(self):
       
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)

        
        element = self.driver.find_element_by_xpath("//span[@class='customRadioBtn']")
        time.sleep(2)
        element.click()
    
            

       
        time.sleep(1)

       


if __name__ == "__main__":
    MMT = MyTrip(base_url)
    MMT.run_script()
    
