from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Set up the WebDriver (using Chrome in headless mode)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        for _ in range(24):  # Run the check 24 times (once per hour)
            # Open the webpage
            url = 'https://test.naxape.com/Naxp/index.html'
            driver.get(url)
            print(f'Opened {url}')
            
            # Perform any necessary checks here
            # Example: check for a specific element
            # element = driver.find_element_by_id("example_id")
            # print(f'Element text: {element.text}')
            
            # Wait for an hour before the next check
            time.sleep(60 * 60)

        print('Finished checking the page periodically')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
