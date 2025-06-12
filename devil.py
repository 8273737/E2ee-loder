from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def send_fb_message():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    
    # लॉगिन करें
    email = driver.find_element_by_id("email")
    email.send_keys("your_email@example.com")
    
    password = driver.find_element_by_id("pass")
    password.send_keys("your_password")
    password.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
    # मैसेज भेजें
    driver.get("https://www.facebook.com/messages/t/username")
    time.sleep(3)
    
    message_box = driver.find_element_by_xpath("//div[@role='textbox']")
    message_box.send_keys("आपका मैसेज")
    message_box.send_keys(Keys.RETURN)
    
    time.sleep(2)
    driver.quit()

# होस्टिंग पर चलाने के लिए समय अंतराल के साथ
while True:
    send_fb_message()
    time.sleep(3600)  # प्रति घंटा 1 मैसेज
