# Author Zahit Dereli

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# open the browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# run the browser in fullscreen
browser.maximize_window()

# go to the url
driver.get("https://practicetestautomation.com/practice-test-login")

# check whether the url is right:
currentURL = driver.current_url
URLtitle = driver.title
# or
if"practice" in currentURL:
    print("thats the right page")

# type username "student" into username field
usernameLocator = driver.find_element(By.ID, "username")
usernameLocator.send_keys("student")
# type password Password123 into password field
passwordLocator = driver.find_element(By.NAME, "password")
passwordLocator.send_keys("Password123")
# push submit button
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_locator.click()

# Verify new page URL contains practicetestautomation.com/logged-in-successfully
currentURL = driver.current_url
assert currentURL == "https://practicetestautomation.com/logged-in-successfully/"
# or
if "successfully" in currentURL:
    print("we're on the right page")

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
linktext = driver.find_element(By.XPATH, "//h1[@class='post-title']").text  # or By.TAG_NAME, "h1"
assert linktext == "Logged In Successfully"
# or
if "Logged" in linktext:
    print("logged in succesfully")

# Verify button Log out is displayed on the new page
logOutButton = driver.find_element(By.LINK_TEXT, "Log out")
assert logOutButton.is_displayed()
# or
if logOutButton:
    print("button is there")
