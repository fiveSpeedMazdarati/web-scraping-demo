import requests
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose


practice_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

result = requests.get(practice_url)

doc = BeautifulSoup(result.text, "html.parser")

span_tags = doc.find_all("span")
print("-----------")
tag_count = len(span_tags)
print(f"There are {tag_count} span tags")
print("-----------")
print("Span tags:")
print(span_tags)
print("-----------")

print(f"This span tag contains the first interesting value: {span_tags[9]}")

index = 9
list_of_tuples = []
while index < len(span_tags) - 1:
    list_of_tuples.append((span_tags[index], span_tags[index + 1], span_tags[index + 2]))
    index += 3

print("Values of interest:")
for tuple in list_of_tuples:
    print(tuple[0].text)
    print(tuple[1].text)
    print(tuple[2].text)
    print("-----------")












