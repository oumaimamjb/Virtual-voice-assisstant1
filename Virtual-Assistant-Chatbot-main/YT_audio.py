import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MusicPlayer:
    def __init__(self):
        # Loading the path of the Chrome WebDriver
        os.environ['PATH'] += ";C:/selenium_drivers"
        
        # Start Chrome WebDriver
        self.driver = webdriver.Chrome()

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        
        # Wait for the video element to be clickable
        try:
            video = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#video-title'))
            )
            video.click()
            print("Video is playing now!")
        except Exception as e:
            print("Error:", e)
