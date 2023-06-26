import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find and print specific elements from the parsed HTML
    # Here's an example of finding all the links on the page:
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))
else:
    print("Failed to retrieve data. Error code:", response.status_code)
