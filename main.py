import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def get_sort_key(data):
    return data[0]


practice_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
eval_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

result = requests.get(eval_url)

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

print(list_of_tuples)
# find the largest x and y values from the tuples
largest_x = 100
largest_y = 8

# Create an empty grid (adjusted to 0-indexed)
grid = [
    [' ' for _ in range(largest_x)]
    for _ in range(largest_y)
]

# Put the characters into the correct places on the grid
for (x, char, y) in list_of_tuples:
    if 0 <= x < largest_x and 0 <= y < largest_y:  # Ensure x and y are within bounds
        grid[y][x] = char

# Print the grid (reversed for proper top-down view)
for row in reversed(grid):
    print(''.join(row))


