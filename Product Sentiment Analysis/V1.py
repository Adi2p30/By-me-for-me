import requests
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context


def scrape_amazon_product(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.find("span", {"id": "productTitle"}).get_text().strip()

        price = soup.find("span", {"class": "a-offscreen"}).get_text().strip()

        rating = soup.find("span", {"class": "a-icon-alt"}).get_text().strip()

        description = soup.find("div", {"id": "productDescription"}).get_text().strip()
        reviews = soup.find_all("div", class_="review")

        for review in reviews:

            review_text = review.find("span", class_="review-text").text

            reviewer_name = review.find("span", class_="reviewer-name").text

            review_rating = review.find("span", class_="review-rating").text

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "description": description,
        }
    else:

        print(response.status_code)
        return None

    rint(f"Reviewer: {reviewer_name}")
    print(f"Rating: {review_rating}")
    print(f"Review: {review_text}")
    print("---")


scrape_amazon_product(
    "https://www.amazon.in/GKI-G-Star-Plastic-Table-Tennis/dp/B078&pd_rd_i=B07FLJQZYR"
)
