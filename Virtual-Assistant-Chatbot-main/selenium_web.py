import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_info(query):
    # Loading the path of the Chrome WebDriver
    os.environ['PATH'] += ";C:/selenium_drivers"
    
    # Start Chrome WebDriver
    driver = webdriver.Chrome()
    
    driver.get("https://wikipedia.org")
    driver.maximize_window()
    
    # Wait for the search input element to be clickable
    search_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="searchInput"]'))
    )
    
    search_input.click()
    search_input.send_keys(query)
    
    # Wait for the search button to be clickable
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="search-form"]/fieldset/button'))
    )
    
    search_button.click()

    # Print the page title using UTF-8 encoding
    print("Page title:", driver.title.encode('utf-8').decode('utf-8', 'ignore'))  

    # Quit the WebDriver
    driver.quit()
