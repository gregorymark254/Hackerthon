from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# selenium script to automate login
def main():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # navigate to the login page
        driver.get("https://stockplus.vercel.app")

        # enter username
        username = driver.find_element(By.ID, "email")
        username.send_keys("greg@gmail.com")

        # enter password
        password = driver.find_element(By.ID, "password")
        password.send_keys("qwerty123")

        # click the login button
        login = driver.find_element(By.XPATH,"//button[@type='submit']")
        login.click()

        # wait for the redirection to the homepage
        time.sleep(5)

        # verify that the user is redirected to the homepage
        url = driver.current_url
        if "/app/dashboard" in url:
            print("--------Login successful!------------")
            print('-----Welcome to the Stock Plus.------')
        else:
            print("Login failed or redirection issue.")

    finally:
        # close the browser window
        driver.quit()


if __name__ == "__main__":
    main()
