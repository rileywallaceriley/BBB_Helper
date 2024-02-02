import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, REQUIRED for Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize WebDriver (webdriver-manager handles the ChromeDriver setup)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Streamlit UI
st.title('BBB Web Scraper')

# Input for code
code = st.text_input('Enter the code:', '')

# Button to trigger scraping
if st.button('Scrape'):
    try:
        # Navigate to the page
        driver.get("https://respond.bbb.org/respond/")
        
        # Enter the code into the input field (adjust the selector as needed)
        input_element = driver.find_element_by_id('input_id')
        input_element.send_keys(code)
        
        # Click the login button (adjust the selector as needed)
        driver.find_element_by_id('login_button_id').click()
        
        # Wait for the content to load
        time.sleep(5)  # Adjust the timing based on page load times
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Extract data (adjust the selector based on your needs)
        data = soup.find('div', {'id': 'content_id'}).get_text(strip=True)
        
        # Display the scraped data in the Streamlit app
        st.write('Scraped Data:', data)
        
    except Exception as e:
        st.error(f'An error occurred: {e}')
    finally:
        driver.quit()

# Close the driver (outside the button press)
driver.quit()
