import requests
from bs4 import BeautifulSoup

def get_max_x(tuples):
    x_values = [t[0] for t in tuples]
    return max(x_values)

def get_max_y(tuples):
    y_values = [t[0] for t in tuples]
    return max(y_values)


practice_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
eval_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

def display_message(url):
    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")

    span_tags = doc.find_all("span")

    print(f"This span tag contains the first interesting value: {span_tags[9]}")

# starting at index 9 of all the span tags
# loop through the remaining span tags
# create a tuple which contains the x, y, and char to display
    index = 9
    list_of_tuples = []
    while index < len(span_tags) - 1:
        list_of_tuples.append((int(span_tags[index].text), span_tags[index + 1].text, int(span_tags[index + 2].text)))
        index += 3

# find the largest x and y values from the tuples so the layout can size dynamically
    x_max = get_max_x(list_of_tuples)
    y_max = get_max_y(list_of_tuples)

    grid = [
        [' ' for _ in range(x_max)]
        for _ in range(y_max)
    ]

# Put the characters into the correct places on the grid
    for (x, char, y) in list_of_tuples:
        if 0 <= x < x_max and 0 <= y < y_max:  # Ensure x and y are within bounds
            grid[y][x] = char

# Print the grid - reversed so things display correctly
    for row in reversed(grid):
        print(''.join(row))

display_message(eval_url)
