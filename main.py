import requests
from bs4 import BeautifulSoup

# practice URL
practice_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

# evaluation URL
evaluation_url =  "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

def get_data(url):
    raw_data = requests.get(url)
    soup = BeautifulSoup(raw_data.content, "html.parser" )
    print(soup.prettify())

    stuff_i_want = soup.find_all("tr", {"class": "c4"})
    print("This is all of the selected tags:")
    print(stuff_i_want)

if __name__ == '__main__':
    get_data(practice_url)



