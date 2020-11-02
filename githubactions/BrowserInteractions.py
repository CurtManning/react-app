import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestBrowserInteractions():

    def test_interactions(self):
        baseUrl = "https://www.ltgc.com/rate-quote/external/residential"
        # modify executable_path
        # driver = webdriver.Firefox(
        #     executable_path="C:\\Users\\curtmanning\\PycharmProjects\\qa_test_tutorial\\drivers\\geckodriver.exe")
        driverLocation = "/home/runner/work/react-app/react-app/drivers/linux/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation

        options = Options()
        options.add_argument("--no-sandbox")  # bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument("--headless")  # overcome limited resource problems
        driver = webdriver.Chrome(options=options, executable_path=driverLocation)

        # driver = webdriver.Chrome(driverLocation)
        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(baseUrl)
        time.sleep(5)
        # Refreshing the browser clears the a popup that only appears in Chrome
        driver.get(baseUrl)

        # Get Title
        title = driver.title
        print("PASS:  Title of the web page is: " + title)
        # Get Current Url
        currentUrl = driver.current_url
        print("PASS:  Current Url of the web page is: " + currentUrl)
        driver.refresh()  # Browser Refresh

        print("PASS:  Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("PASS:  Browser Refreshed 2nd time")
        # Open another Url
        driver.get("https://www.ltgc.com/rates/calc")
        currentUrl = driver.current_url
        print("PASS:  Current Url of the web page is: " + currentUrl)
        # Browser Back
        driver.back()
        print("PASS:  Go one step back in browser history")
        currentUrl = driver.current_url
        print("PASS:  Current Url of the web page is: " + currentUrl)
        # Browser Forward
        driver.forward()
        print("PASS:  Go one step forward in browser history")
        currentUrl = driver.current_url
        print("PASS:  Current Url of the web page is: " + currentUrl)
        # Get Page Source
        # pageSource = driver.page_source
        # print("PASS:  PageSource " + str(pageSource))
        # Browser Close / Quit
        # driver.close()
        # driver.quit()


ff = TestBrowserInteractions()
ff.test_interactions()
