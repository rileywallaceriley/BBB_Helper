import httpx
from bs4 import BeautifulSoup
import streamlit as st

# Streamlit UI setup
st.title('BBB Response Page Scraper')

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
                'input_name': code  # Replace 'input_name' with the actual name of the input field
            }
            
            # Simulate form submission (POST request)
            response = httpx.post(url, data=data)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the page content with BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract and display specific data (adjust the selector based on your needs)
                # Example: Extract text from a div with id 'content_id'
                data = soup.find('div', {'id': 'content_id'}).get_text(strip=True)
                
                # Display the scraped data in the Streamlit app
                st.write('Scraped Data:', data)
            else:
                st.error(f'Failed to retrieve the webpage. Status code: {response.status_code}')
            
        except Exception as e:
            st.error(f'An error occurred: {e}')
    else:
        st.error('Please enter a code to scrape.')

