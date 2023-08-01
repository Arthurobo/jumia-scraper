import csv
from bs4 import BeautifulSoup
import requests


category_urls = [
    "https://www.jumia.com.ng/electronics/?page=1#catalog-listing",
    "https://www.jumia.com.ng/health-beauty/?page=1#catalog-listing"
]

# Specify the range of pages you want to add
start_page = 1
end_page = 3

# List of categories
categories = ["electronics", "health-beauty"]

# Generate and append the URLs to the category_urls list
for category_url in category_urls:
    base_url = category_url.split("?")[0]  # Extract the base URL without the page parameter
    for page in range(start_page, end_page + 1):
        url = f"{base_url}?page={page}#catalog-listing"
        category_urls.append(url)

# Print the updated category_urls list
print(category_urls)






"""

# category_urls = ["https://www.jumia.com.ng/electronics/?page=1#catalog-listing",]


urls = [
    # "https://www.jumia.com.ng/electronics/?page=1#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=2#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=3#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=4#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=5#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=6#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=7#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=8#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=9#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=10#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=11#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=12#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=13#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=14#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=15#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=16#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=17#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=18#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=19#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=20#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=21#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=22#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=23#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=24#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=25#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=26#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=27#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=28#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=29#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=30#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=31#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=32#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=33#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=34#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=35#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=36#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=37#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=38#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=39#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=40#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=41#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=42#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=43#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=44#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=45#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=46#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=47#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=48#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=49#catalog-listing",
    # "https://www.jumia.com.ng/electronics/?page=50#catalog-listing",




    "https://www.jumia.com.ng/health-beauty/?page=1#catalog-listing"
    "https://www.jumia.com.ng/health-beauty/?page=2#catalog-listing"
]

all_product_details_urls = []


for url in urls:
    url = url

    # Send a GET request to the URL
    response = requests.get(url)

    # Get the HTML content
    html_content = response.content

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the <article> tags with class "c-prd"
    article_tags = soup.find_all('article', class_='c-prd')

    # Iterate over the article tags
    for article_tag in article_tags:
        # Find the first <a> tag within the current article tag
        a_tag = article_tag.find('a')

        # Check if the <a> tag exists
        if a_tag and 'href' in a_tag.attrs:
            # Extract the link from the href attribute
            link = a_tag['href']

            # Print the link
            print(link)
            cleaned_link = str("https://jumia.com.ng" + str(link))
            all_product_details_urls.append(cleaned_link)

# print(all_product_details_urls)

# Append the links to an existing CSV file
csv_filename = "links.csv"
with open(csv_filename, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([[link] for link in all_product_details_urls])

print(f"Links are appended to {csv_filename}.")
print(len(all_product_details_urls))


"""