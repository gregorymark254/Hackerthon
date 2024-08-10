from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# selenium script to search for Test Automation in google and verifies that it contains data
def main():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # open google
        driver.get("https://www.google.com")

        # find the search box
        search = driver.find_element("name", "q")

        # type the query
        search.send_keys("Test Automation")

        # submit the results
        search.send_keys(Keys.RETURN)

        # wait for results
        time.sleep(5)
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        found = any("test automation" in result.text.lower() for result in results)

        if found:
            print("-----Found test automation-----")
        else:
            print("-----TEST AUTOMATION NOT FOUND-----")

    finally:
        # close the browser window
        driver.quit()


if __name__ == "__main__":
    main()
