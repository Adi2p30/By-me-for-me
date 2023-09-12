import requests
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
def scrape_amazon_product(url):
    # Send a GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the product title
        title = soup.find('span', {'id': 'productTitle'}).get_text().strip()

        # Extract the product price
        price = soup.find('span', {'class': 'a-offscreen'}).get_text().strip()

        # Extract the product rating
        rating = soup.find('span', {'class': 'a-icon-alt'}).get_text().strip()

        # Extract the product description
        description = soup.find('div', {'id': 'productDescription'}).get_text().strip()
        reviews = soup.find_all('div', class_='review')

        for review in reviews:
            # Extract the review text
            review_text = review.find('span', class_='review-text').text

            # Extract the reviewer's name
            reviewer_name = review.find('span', class_='reviewer-name').text

            # Extract the review rating
            review_rating = review.find('span', class_='review-rating').text

            # Print the review details
            

        # Return the scraped product information as a dictionary
        return {
            'title': title,
            'price': price,
            'rating': rating,
            'description': description
        }
    else:
        # If the request was not successful, return None
        print(response.status_code)
        return None

    rint(f'Reviewer: {reviewer_name}')
    print(f'Rating: {review_rating}')
    print(f'Review: {review_text}')
    print('---')
scrape_amazon_product("https://www.amazon.in/GKI-G-Star-Plastic-Table-Tennis/dp/B078&pd_rd_i=B07FLJQZYR")