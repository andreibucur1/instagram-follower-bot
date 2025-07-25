from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""

class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        cookies_button = self.driver.find_elements(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
        if cookies_button:
            cookies_button[0].click()

        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD + Keys.ENTER)

        time.sleep(4)

        try:
            self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(8)

        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()
