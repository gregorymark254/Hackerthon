from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time


def main():
    desired_cap = {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'appPackage': 'com.example.app',
        'appActivity': '.MainActivity',
        'automationName': 'UiAutomator2',
        'noReset': True
    }

    driver = webdriver.Remote('https://stockplus.vercel.app', desired_cap)

    try:
        # Wait for the app to launch
        time.sleep(5)

        # log in using email and password
        email_field = driver.find_element(MobileBy.ID, 'com.example.app:id/email')
        password_field = driver.find_element(MobileBy.ID, 'com.example.app:id/password')
        login_button = driver.find_element(MobileBy.ID, 'com.example.app:id/login_button')

        email_field.send_keys('test@example.com')
        password_field.send_keys('password123')
        login_button.click()

        # Wait for login to complete
        time.sleep(5)


        settings_button = driver.find_element(MobileBy.ACCESSIBILITY_ID,
                                              'Settings')
        settings_button.click()

        # Wait for settings page to load
        time.sleep(3)

        profile_edit_button = driver.find_element(MobileBy.ID,
                                                  'com.example.app:id/edit_profile_button')
        profile_edit_button.click()

        name_field = driver.find_element(MobileBy.ID, 'com.example.app:id/name')
        name_field.clear()
        name_field.send_keys('New Name')

        save_button = driver.find_element(MobileBy.ID, 'com.example.app:id/save_button')
        save_button.click()

        success_message = driver.find_element(MobileBy.ID, 'com.example.app:id/success_message')
        assert success_message.is_displayed(), "Profile update failed."

        print("Profile updated successfully.")

    finally:
        # Close the app and end the session
        driver.quit()


if __name__ == "__main__":
    main()
