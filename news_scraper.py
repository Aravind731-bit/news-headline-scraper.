import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://news.ycombinator.com/"

# Send request to website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all headlines
headlines = soup.find_all("span", class_="titleline")

# Save headlines to text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    print("Top Headlines:\n")

    for i, headline in enumerate(headlines, start=1):
        title = headline.get_text()
        print(f"{i}. {title}")
        file.write(f"{i}. {title}\n")

print("\nHeadlines saved to headlines.txt")
