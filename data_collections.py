import requests
from bs4 import BeautifulSoup

def scrape_business_details(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the elements containing business details
        business_details = soup.find_all('div', class_='rj_ser_det')
        
        # Iterate over each business detail element
        for detail in business_details:
            # Extract specific details (you may need to adjust this based on the webpage structure)
            name = detail.find('h3',class_="name-icon xxlarge black fw6 mb-2 sc").text.strip()
            address = detail.find('p', class_='dul mb-1').text.strip()
            deals = detail.find('p', class_='gray lh14em large').text.strip()
            # Print or store the extracted details
            print(f"Name: {name}\nAddress: {address}\nDeals With: {deals}")
            print("")
    else:
        print("Failed to retrieve page")

# URL of the webpage containing business details
url = 'https://www.indianyellowpages.com/neemuch/'

# Call the function to scrape business details from the URL
scrape_business_details(url)