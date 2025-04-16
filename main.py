import requests
from bs4 import BeautifulSoup

def get_data(url):
    raw_data = requests.get("https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub")
    soup = BeautifulSoup(raw_data.content, "html.parser" )
    print(soup.prettify())

    stuff_i_want = soup.find_all("tr", {"class": "c4"})
    print("This is all of the selected tags:")
    print(stuff_i_want)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    get_data("")

