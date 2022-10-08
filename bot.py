from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 

s = Service("C:\\Users\\peter\\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://linkedin.com")

time.sleep(2)

username = driver.find_element("xpath", "//input[@name='session_key']")
password = driver.find_element("xpath", "//input[@name='session_password']")

username.send_keys("peternick0207@gmail.com")
password.send_keys("Kite870920!")

time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']").click()

time.sleep(2)
nb_pages = 3

for p in range(1, nb_pages):

    driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B%221441%22%5D&geoUrn=%5B%22103644278%22%5D&origin=FACETED_SEARCH&page=" + str(p) + "&schoolFilter=%5B%223382%22%5D&sid=Em%2C")
    time.sleep(2) 
    
    all_buttons = driver.find_elements(By.XPATH, "//button[starts-with(@class, 'artdeco-button')]") 
    
    all_names = driver.find_elements(By.TAG_NAME, "span")
    all_names = [s for s in all_names if s.get_attribute("aria-hidden") == "true"]
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    for i in range(0, len(connect_buttons)):

        driver.execute_script("arguments[0].click();", connect_buttons[i])
        
        add_button = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
        driver.execute_script("arguments[0].click();", add_button)
        
        paragraph = driver.find_element(By.XPATH, "//textarea[@id='custom-message']")
        paragraph.send_keys("hi")

        time.sleep(2)
        
        
        #submit = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
        #driver.execute_script("arguments[0].click();", submit)
        
        dismiss_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", dismiss_button)
        
        time.sleep(2)
            
                
#        paragraphs[0].send_keys("Hi, this is Benjamin. I didnt mean to bother you. I am building my linkedin automated messaging bot, and I am testing it. Hope you don't mind :)! Have a wonderful day!")
#        time.sleep(2)

#         #submit = driver.find_element(By.XPATH, "//button[@type='submit']")
#         #driver.execute_script("arguments[0].click();", submit)
#         #time.sleep(2)

#         close_button = driver.find_element(By.XPATH, "//button[@class='msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']")
#         driver.execute_script("arguments[0].click();", close_button)
#         time.sleep(2)

#         discard_button = driver.find_element(By.XPATH, "//button[@class='artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
#         driver.execute_script("arguments[0].click();", discard_button)
#         time.sleep(2)