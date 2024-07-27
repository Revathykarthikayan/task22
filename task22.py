from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Set up the Chrome WebDriver
chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for no browser UI
options.add_argument('--disable-gpu')# Run in disabled graphical processing unit mode
options.add_argument('--no-sandbox') # Run in no sandbox from the website


# Open the Instagram profile page
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

url = 'https://www.instagram.com/guviofficial/'
driver.get(url)

# Wait for the page to load
time.sleep(5)

try:
    # Locate the followers and following elements by their XPaths
    followers_element = driver.find_element(By.XPATH,"//header//ul/li[2]//span")
    following_element = driver.find_element(By.XPATH,"//header//ul/li[3]//span" )

    # Get the counts
    followers_count = followers_element.get_attribute('title')
    following_count = following_element.text

    print(f"Followers: {followers_count}")
    print(f"Following: {following_count}")
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    driver.quit()


