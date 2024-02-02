import httpx
from bs4 import BeautifulSoup
import streamlit as st

# Streamlit UI setup
st.title('BBB Response Portal Scraper')

# Input for the code
code = st.text_input('Enter the code:', '')

# Button to trigger form submission and scraping
if st.button('Submit and Scrape'):
    if code:
        try:
            # Endpoint where the form data is sent
            url = 'https://respond.bbb.org/respond/'

            # Data payload for the form
            data = {
                'cd': code  # The name of the input field for the code
            }
            
            # Headers may be required for the server to accept the request
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://respond.bbb.org/respond/'
            }
            
            # Simulate form submission (POST request)
            with httpx.Client() as client:
                response = client.post(url, data=data, headers=headers)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the page content with BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract and display specific data (adjust the selector based on your needs)
                # Example: Extract text from a specific div
                data = soup.find('div', {'id': 'specific_id'}).get_text(strip=True)  # Adjust the ID to your target
                
                # Display the scraped data in the Streamlit app
                st.write('Scraped Data:', data)
            else:
                st.error(f'Failed to retrieve the webpage. Status code: {response.status_code}')
            
        except Exception as e:
            st.error(f'An error occurred: {e}')
    else:
        st.error('Please enter a code to scrape.')
