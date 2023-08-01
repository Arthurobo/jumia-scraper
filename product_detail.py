from bs4 import BeautifulSoup
import requests

url = "https://www.jumia.com.ng/weyon-43-inches-led-tv-43wan-black-1-year-warranty-136644248.html"  # Replace with the actual URL

# Send a GET request to the URL
response = requests.get(url)

# Get the HTML content
html_content = response.content

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the <div> tag with class "-prl"
div_tag = soup.find('div', class_="-prl")

# Find the <h1> tag with class "-fs20" within the <div> tag
h1_tag = div_tag.find('h1', class_="-fs20")

# Check if the <h1> tag exists
if h1_tag:
    # Extract the text within the <h1> tag
    data = h1_tag.get_text()
    print(data)
else:
    print("Data not found.")
