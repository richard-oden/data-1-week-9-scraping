import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_monarchs_df() -> pd.DataFrame:
    return pd.read_html('https://en.wikipedia.org/wiki/List_of_British_monarchs', attrs={'class': 'wikitable'})[0]

# Scraping search results using beautiful soup
# https://louisville.craigslist.org/search/apa?min_price=&max_price=900&max_bedrooms=1&availabilityMode=0&sale_date=all+dates
def print_apartments_info() -> None:
    response = requests.get('https://louisville.craigslist.org/search/apa?min_price=&max_price=600&max_bedrooms=1&availabilityMode=0&sale_date=all+dates')

    # BeautifulSoup allows us to more easily parse our HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # here we're getting all elements with the CSS class 'result-row'.
    result_rows = soup.select('.result-row')

    for result_row in result_rows:

    # now we're searching each result_row for a title, location, and price using CSS classes
        title_element = result_row.select_one('.result-title')
        location_element = result_row.select_one('.result-hood')
        price_element = result_row.select_one('.result-price')

        # if title_element, location_element, or price_element are None, then we skip this result_row
        if (None in [title_element, location_element, price_element]):
            continue

        print(f'\n- {title_element.text}')
        print(f'  location: {location_element.text}')
        print(f'  rent: {price_element.text}')

print_apartments_info()