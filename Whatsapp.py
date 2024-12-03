import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def hack_whatsapp(phone_number, message):
    # Set up the web driver
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")

    # Wait for the QR code to be scanned
    time.sleep(15)

    # Find the search box and enter the target phone number
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    time.sleep(2)

    # Select the target contact
    contact = driver.find_element(By.XPATH, f'//span[@title="{phone_number}"]')
    contact.click()
    time.sleep(2)

    # Find the message box and send the message
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

    # Close the web driver
    driver.quit()

# Example usage
phone_number = "+1234567890"  # Replace with the target phone number
message = "Hello, this is a threat message! Please stop sending me messages."
hack_whatsapp(phone_number, message)
