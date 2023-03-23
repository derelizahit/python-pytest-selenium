import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative

    def test_negative_username(self):

########## INCORRECT USERNAME LOGIN TEST

        # Open page
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(2)
        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed"
        # Verify error message text is Your username is invalid!
        error_message = error_locator.text
        if "Your username is invalid" in error_message:
            print("error message is right")
        assert error_message == "Your username is invalid!", "Error message is not expected!"

########## INCORRECT PASSWORD LOGIN TEST


    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self):
        # Open page
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login")
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password")
        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(2)
        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed"
        # Verify error message text is Your password is invalid!
        error_message = error_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected!"




