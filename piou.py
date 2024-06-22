from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (using Chrome in headless mode)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the webpage
    url = 'https://test.naxape.com/Naxp/index.html'
    driver.get(url)
    print(f'Opened {url}')

    # Keep the page open for a specified duration (e.g., 1 minute)
    time.sleep(24 * 60 * 60)  # Keep the page open for 60 seconds (1 minute)

    print('Finished keeping the page open')
finally:
    # Close the browser
    driver.quit()
